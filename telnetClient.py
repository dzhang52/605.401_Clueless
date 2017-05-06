# telnet program example
import socket, select, string, sys, os, errno
import threading
from thread import *
from time import sleep
import newGame
import BoardGUI
from BoardGUI import *
from newGame import *


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

  gameGUI = QApplication(sys.argv)
  new = newGame.startup()
  gui = BoardGUI()
  new.show()
  gameGUI.exec_()
  count = 0

  host = "127.0.0.1"
  port = 5555

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # connect to remote host
  try:
    s.connect((host, port))
  except:
    print('Unable to connect')
    sys.exit()

  print('Connected to remote host')

  start_new_thread(threaded_inputListener, (s,))  # python2
  res = new.res_assignment()
  while count == 0:
    sleep(1)
    print(new.name_assignment())
    s.send(new.name_assignment())
    sleep(1)
    print("Start Game")
    s.send("Start Game")
    sleep(1)
    print(new.player_assignment())
    s.send(new.player_assignment())
    count = 1
  print("res0: " + res[0])
  print("res1: " + res[1])
  gui.resolution(res[0], res[1])
  gui.init_ui()
  gui.show()

  while True:
    i = 1
    print('test')
  #while True:



