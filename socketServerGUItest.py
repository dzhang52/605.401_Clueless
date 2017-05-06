import socket
import sys
import errno
import threading
# import Queue

from thread import *
from game import *
from player import *
from cards import *


globalReply = ""
count = 0
# q = Queue()
queueLock = threading.Lock()


class threadedClient(threading.Thread):
  def __init__(self, threadID, name, conn, addr):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name

    global globalReply
    global count

  def run(self):
    print("Starting " + self.name)

    # main part of the method
    conn.send('Welcome, type your info\n')
    conn.send('There are ' + str(count) + ' player(s) in the game')

    while True:
      try:
        data = conn.recv(4096)
        queueLock.acquire()
        globalReply = 'Server: ' + data
        queueLock.release()
        if not data:
          print('Connection closed')
          break
        conn.sendall(globalReply)
        print('Request from ' + str(addr[0]) + ':' + str(addr[1]) + ':' + data)
      except socket.error as e:
        if e.errno == errno.WSAECONNRESET:
          print('A player has left')
          quit()

    print('Connection closing')
    conn.close()
    # end of the main part of the method

    print("Exiting " + self.name)


def threaded_client(conn, addr):
  conn.send("Welcome. To start a game, type 'Start Game'\n")

  global globalReply
  global count

  while "Start Game" not in globalReply and "End child processes" not in globalReply:
    try:
      conn.setblocking(0)  # Cannot set blocking mode
      data = conn.recv(4096)
      queueLock.acquire()
      globalReply = 'Server: ' + data
      queueLock.release()
      if not data:
        print('Connection closed')
        break
      conn.sendall(globalReply)
      print('Request from ' + str(addr[0]) + ':' + str(addr[1]) + ':' + data)
    except socket.error as e:
      if e.errno == errno.WSAECONNRESET:
        print('A player has left')
        quit()

  queueLock.acquire()
  count -= 1
  queueLock.release()

  print('Terminating threaded_client for ' + str(addr[0]) + ':' + str(addr[1]) + '.\n')

  if count == 0:
    queueLock.acquire()
    globalReply = "Starting Game"
    queueLock.release()
    # print('Connection closing')
    # conn.close()


def getPlayerInput(firstArg, message):
  if hasattr(firstArg, 'conn'):
    conn = firstArg.conn
  else:
    conn = firstArg

  conn.send(message)
  conn.setblocking(1)
  data = conn.recv(4096)
  return data
  # try:
  #     data = conn.recv(4096)
  # except socket.error as e:
  #         if e.errno == errno.WSAECONNRESET:
  #             print('An error occured in getPlayerInput()')

  print("End of getPlayerInput")


def printAll(players, message):
  # message += '\n'

  for player in players:
    player.conn.sendall(str(message) + '\n')

  print(message)


def printToPlayer(player, message):
  # str += '\n'

  player.conn.sendall(str(message) + '\n')


# main function
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
  print('Waiting for connections.')

  conns = []
  addrs = []
  players = []




  # q.put(globalReply)
  while count < 6 and "Starting Game" not in globalReply:
    try:
      conn, addr = s.accept()
      print('connected to: ' + addr[0] + ':' + str(addr[1]))
      name = getPlayerInput(conn, "Please enter your name:")
      players.append(Player(conn, addr, name))

      # conns.append(conn)
      # addrs.append(addr)

      # threading.Thread(target=threaded_client, args=(conn,addr,)).start() #python3
      start_new_thread(threaded_client, (conn, addr,))  # python2
      # thread = threadedClient(count, "Thread-" + str(count), conn, addr)
      count += 1
      print("There are %d player(s) in the game" % count)
      # thread.start()

    except socket.error as e:
      pass

  globalReply = "End child processes"

  while count != 0:
    pass

  queueLock.acquire()
  globalReply = ''
  queueLock.release()

  printAll(players, "Starting a game of Clue-less")

  gameBoard = GameBoard()
  gameBoard.initialize()
  printAll(players, gameBoard.printBoard())

  characters = gameBoard.characters
  for player in players:
    while player.character == '':
      printToPlayer(player, "Select a character from the following:")
      charCounter = 0
      for character in characters:
        printToPlayer(player, str(charCounter) + ". " + character.name)
        charCounter += 1
      try:
        charIdx = int(getPlayerInput(player, "Please enter the index of the character: "))
        player.character = characters[charIdx]
      except Exception:
        printToPlayer(player, "Please enter a valid input")
    del characters[charIdx]

  cardDeck = CardDeck()
  secretEnvelope = cardDeck.dealSecretEnvelope()

  print("secretEnvelope: " + str(secretEnvelope))

  cardDeck.dealCards(players)

  for player in players:
    printToPlayer(player, player.cards)

  while True:
    if globalReply != '':
      print("globalReply: " + globalReply)
      globalReply = ''
