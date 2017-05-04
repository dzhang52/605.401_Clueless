# telnet program example
import socket, select, string, sys, os, errno
import threading
from thread import *
from BoardGUI import *


def threaded_inputListener(conn):
  while True:
    try:
      data = conn.recv(4096)
      if not data:
        print('Connection closed')
        sys.exit()
      else:
        sys.stdout.write(data)
    except socket.error as e:
      if e.errno == errno.WSAECONNRESET:
        print('Server is down')
        # interrupt_main()
        os._exit(1)


# main function
if __name__ == "__main__":

  if (len(sys.argv) < 3):
    print('Usage : python telnet.py hostname port')
    sys.exit()

  host = sys.argv[1]
  port = int(sys.argv[2])

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # s.settimeout(2)

  # connect to remote host
  try:
    s.connect((host, port))
  except:
    print('Unable to connect')
    sys.exit()

  print('Connected to remote host')

  # threading.Thread(target=threaded_inputListener, args=(s,)).start() #python3
  start_new_thread(threaded_inputListener, (s,))  # python2

  while True:
    app = QtWidgets.QApplication(sys.argv)
    gameBoardGUI = BoardGUI()
    gameBoardGUI.init_ui()
    app.exec_()

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

    msg = sys.stdin.readline()
    s.send(msg)