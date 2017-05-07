# telnet program example
import socket, select, string, sys, os, errno
import threading
import time

from thread import *

from BoardGUI import *
from newGame import *

from PySide.QtCore import *
from PySide.QtGui import *

queueLock = threading.Lock()

globalResponse = ""

 
def threaded_globalInputListener(conn):
    print("Starting globalInputListener()")

    global globalResponse

    while "End gloalInputListener" not in globalResponse:
        try:
            #print("globalResponse from thread: " + globalResponse)
            data = conn.recv(4096)
            queueLock.acquire()
            globalResponse = 'Server: ' + data
            queueLock.release()
            if not data:
                print('Connection closed')
                sys.exit()
            else:
                sys.stdout.write(data)
        except socket.error as e:
            if e.errno == errno.WSAECONNRESET:
                print('Server is down')
                #interrupt_main()
                os._exit(1)

    print("Ending globalInputListener()")

def threaded_localInputListener(conn):

    print("Starting localInputListener()")

    while True:
        try:
            data = conn.recv(4096)
            if not data:
                print('Connection closed')
                sys.exit()
            else:
                #sys.stdout.write(data)
                dataList = data.split(",")
        except socket.error as e:
            if e.errno == errno.WSAECONNRESET:
                print('Server is down')
                #interrupt_main()
                os._exit(1)

    print("Ending localInputListener()")
    
def threaded_applicationUpdate(application):
    global globalResponse

    while "End child processes" not in globalResponse:
        pass
    #time.sleep(2)
    application.updateFromServer()
    #application.printGlobalMessage()

def sendToServer(socketS, message):
    socketS.send(message)
    return ""

#def startGui():

def threaded_getGameUpdate(socketS, boardGUI):

    print("Starting threaded_getGameUpdate()")

    while True:
        try:
            data = socketS.recv(4096)
            if not data:
                print('Connection closed')
                sys.exit()
            else:
                #sys.stdout.write(data)
                if "Char Update-" in data:
                    data.replace('Char Update-','')
                    charList = data.split(";")
                    charList.pop()
                    for charItem in charList:
                        char = charItem.split(":")
                        charName = char[0]
                        charPos = char[1].split(",")
                        boardGUI.player_setup(charName, int(charPos[0]), int(charPos[1]))
                    
        except socket.error as e:
            if e.errno == errno.WSAECONNRESET:
                print('Server is down')
                #interrupt_main()
                os._exit(1)

    print("Ending threaded_getGameUpdate()")
    
def getBoardUpdate(socketS, message):
    print "waiting for board update"
    try:
        s.setblocking(1)
        data = s.recv(4096)
        if not data:
            print('Connection closed')
            sys.exit()
        else:
            #sys.stdout.write(data)
            dataList = data.split(",")
            enterCharWindow = EnterCharWindow(s, dataList)
            enterCharWindow.show()
            app.exec_()
    except socket.error as e:
        if e.errno == errno.WSAECONNRESET:
            print('Server is down')
            #interrupt_main()
            os._exit(1)

    

#main function
if __name__ == "__main__":

    if(len(sys.argv) < 3) :
        print('Usage : python telnet.py hostname port')
        sys.exit()
     
    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.05)
    #s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print('Unable to connect')
        sys.exit()
     
    print('Connected to remote host')

    start_new_thread(threaded_globalInputListener,(s,)) #python2

    app = QApplication(sys.argv)

    #msg = sys.stdin.readline()
    #msg = sendToServer(s, msg)
    enterNameWindow = EnterNameWindow(s)
    enterNameWindow.show()
    app.exec_()
    
    
    startupWindow = StartupWindow(s)
    start_new_thread(threaded_applicationUpdate,(startupWindow,))
    startupWindow.show()
    app.exec_()
    
    time.sleep(1)
    print "start while loop"
    print "globalResponse: " + globalResponse

    globalResponse = "End gloalInputListener"

    #start_new_thread(threaded_localInputListener,(s,)) 
    print "waiting to pick your charcater"
    try:
        s.setblocking(1)
        data = s.recv(4096)
        if not data:
            print('Connection closed')
            sys.exit()
        else:
            #sys.stdout.write(data)
            dataList = data.split(",")
            enterCharWindow = EnterCharWindow(s, dataList)
            enterCharWindow.show()
            app.exec_()
    except socket.error as e:
        if e.errno == errno.WSAECONNRESET:
            print('Server is down')
            #interrupt_main()
            os._exit(1)

    gui = BoardGUI()
    gui.resolution(1366, 768)
    gui.init_ui()
    gui.show()
        
    #gui.player_setup()
    #gui.weapon_setup()
    #start_new_thread(threaded_getGameUpdate,(s,gui,))
    # setup characters
    try:
        data = s.recv(4096)
        if not data:
            print('Connection closed')
            sys.exit()
        else:
            #sys.stdout.write(data)
            if "Char Update-" in data:
                print "before replace: " + data
                data = data.replace('Char Update-','')
                print "after replace: " + data
                charList = data.split(";")
                charList.pop()
                for charItem in charList:
                    char = charItem.split(":")
                    charName = char[0]
                    charPos = char[1].split(",")
                    print("charName: " + charName + ": " + charPos[0] + ", " +  charPos[1])
                    gui.player_setup(charName, int(charPos[0]), int(charPos[1]))
    except socket.error as e:
        if e.errno == errno.WSAECONNRESET:
            print('Server is down')
            #interrupt_main()
            os._exit(1)

    # setup weapons
    try:
        data = s.recv(4096)
        if not data:
            print('Connection closed')
            sys.exit()
        else:
            #sys.stdout.write(data)
            if "Weapon Update-" in data:
                print "before replace: " + data
                data = data.replace('Weapon Update-','')
                print "after replace: " + data
                weaponList = data.split(";")
                weaponList.pop()
                for weaponItem in weaponList:
                    weapon = weaponItem.split(":")
                    weaponName = weapon[0]
                    weaponPos = weapon[1].split(",")
                    print("weaponName: " + weaponName + ": " + weaponPos[0] + ", " +  weaponPos[1])
                    gui.weapon_setup(weaponName, int(weaponPos[0]), int(weaponPos[1]))
                
    except socket.error as e:
        if e.errno == errno.WSAECONNRESET:
            print('Server is down')
            #interrupt_main()
            os._exit(1)

    #gui.init_ui()
    #gui.show()
    app.exec_()
    
    #s.send("Start Game")
    while True:
        
        '''
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print 'Connection closed'
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
             
            #user entered a message
            else :
                msg = sys.stdin.readline()
                s.send(msg)
        '''

        # msg = sys.stdin.readline()
        # s.send(msg)
        
        # if msg != "":
        #    sendToServer(s,msg)