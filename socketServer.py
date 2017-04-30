import socket
import sys
import errno
import threading
import Queue

from thread import *
from game import *

globalReply = ""
count = 0
#q = Queue()
queueLock = threading.Lock()

class threadedClient(threading.Thread):
    def __init__(self, threadID, name, conn, addr):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

        global globalReply
        global count

    def run(self):
        print "Starting " + self.name

        # main part of the method
        conn.send('Welcome, type your info\n')
        conn.send('There are ' + str(count) + ' player(s) in the game')
        

        while True:
            try:
                data = conn.recv(4096)
                queueLock.acquire()
                globalReply = 'Server: '+ data
                queueLock.release()
                if not data:
                    print 'Connection closed'
                    break
                conn.sendall(globalReply)
                print('Request from ' + str(addr[0]) + ':' + str(addr[1]) + ':' + data)
            except socket.error as e:
                if e.errno == errno.WSAECONNRESET:
                    print 'A player has left'
                    quit()
            
        
        print('Connection closing')
        conn.close()
        # end of the main part of the method

        print "Exiting " + self.name
        


def threaded_client(conn, addr):
    conn.send("Welcome. To start a game, type 'Start Game'\n")

    global globalReply
    global count

    while True:
        try:
            data = conn.recv(4096)
            queueLock.acquire()
            globalReply = 'Server: '+ data
            queueLock.release()
            if not data:
                print 'Connection closed'
                break
            conn.sendall(globalReply)
            print('Request from ' + str(addr[0]) + ':' + str(addr[1]) + ':' + data)
        except socket.error as e:
            if e.errno == errno.WSAECONNRESET:
                print 'A player has left'
                quit()
        
    
    print('Connection closing')
    conn.close()

def printAll(conns, str):
    str += '\n'
       
    for conn in conns:
        conn.sendall(str)

    print str
    
#main function
if __name__ == "__main__":

    host = ''
    port = 5555
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((host, port))
    except socket.error as e:
        print(str(e))

    s.settimeout(0.05)
    s.listen(6)
    print('Waiting for a connection.')

    conns = []
    addrs = []

    #q.put(globalReply)
    while count<6 and "Start Game" not in globalReply:
        try:
            conn, addr = s.accept()
            conns.append(conn)
            addrs.append(addr)
            print('connected to: '+addr[0]+':'+str(addr[1]))

            start_new_thread(threaded_client,(conn,addr,))
            #thread = threadedClient(count, "Thread-" + str(count), conn, addr)
            count += 1
            print "There are %d player(s) in the game" % count
            #thread.start()
            
        except socket.error as e:
            pass
       

    queueLock.acquire()
    globalReply = ''
    queueLock.release()

    printAll(conns, "Starting a game of Clue-less")

    gameBoard = GameBoard()
    gameBoard.initialize()
    printAll(conns, gameBoard.printBoard())

    while True:
        if globalReply != '':
            print "globalReply: " + globalReply
            #sys.stdout.flush()
            globalReply = ''
        #print "not listening anymore"
            