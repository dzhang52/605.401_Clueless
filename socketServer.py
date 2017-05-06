import socket
import sys
import errno
import threading
import copy
#import Queue

from thread import *
from game import *
from player import *
from cards import *

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
        print("Starting " + self.name)

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
            conn.setblocking(0) # Cannot set blocking mode
            data = conn.recv(4096)
            queueLock.acquire()
            globalReply = 'Server: '+ data
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
    count-=1
    queueLock.release()

    print('Terminating threaded_client for ' + str(addr[0]) + ':' + str(addr[1]) + '.\n')

    if count == 0:
        queueLock.acquire()
        globalReply = "Starting Game"
        queueLock.release()
    #print('Connection closing')
    #conn.close()

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

def selectFromList(player, list, attr='__str__', callable=True):
    validInput = False
    while True:
        printToPlayer(player, "Select one from the followings:")
        counter = 0
        for item in list:
            if callable:
                printToPlayer(player, str(counter) + ". " + getattr(item, attr)())
            else:
                printToPlayer(player, str(counter) + ". " + getattr(item, attr))
            counter+=1
        try:
            index = int(getPlayerInput(player, "Please enter the index of the desired option: "))
            if callable:
                printToPlayer(player, "You selected " + getattr(list[index], attr)() + "\n")
            else:
                printToPlayer(player, "You selected " + getattr(list[index], attr) + "\n")

            return list[index]
        except Exception:
            printToPlayer(player, "Please enter a valid input")

def printAll(players, message):
    #message += '\n'
       
    for player in players:
        player.conn.sendall(str(message) + '\n')

    print(message)

def printToPlayer(player,message):
    #str += '\n'

    player.conn.sendall(str(message) + '\n')
    

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
    print('Waiting for connections.')

    conns = []
    addrs = []
    players = []

    #q.put(globalReply)
    while count<6 and "Starting Game" not in globalReply:
        try:
            conn, addr = s.accept()
            print('connected to: '+addr[0]+':'+str(addr[1]))
            name = getPlayerInput(conn,"Please enter your name: ").strip()
            players.append(Player(conn, addr, name))

            #conns.append(conn)
            #addrs.append(addr)

            #threading.Thread(target=threaded_client, args=(conn,addr,)).start() #python3
            start_new_thread(threaded_client,(conn,addr,)) #python2
            #thread = threadedClient(count, "Thread-" + str(count), conn, addr)
            count += 1
            print("There are %d player(s) in the game" % count)
            #thread.start()
            
        except socket.error as e:
            pass
       
    globalReply = "End child processes"

    while count!=0:
        pass

    queueLock.acquire()
    globalReply = ''
    queueLock.release()

    printAll(players, "Starting a game of Clue-less")

    gameBoard = GameBoard()
    gameBoard.initialize()
    printAll(players, gameBoard.printBoard() + "\n")

    #playerInput = getPlayerInput(players[0], "Test getPlayerInput()\n")
    #print("playerInput: " + playerInput)

    # Assign characters to players
    characters = copy.deepcopy(gameBoard.characters)
    for player in players:

        char = selectFromList(player, characters, 'name', False)
        for originalChar in gameBoard.characters:
            if originalChar.name == char.name:
                player.character = originalChar
                break
        characters.remove(char)

    # Assign cards to the secret Envelope
    cardDeck = CardDeck()
    secretEnvelope = cardDeck.dealSecretEnvelope()

    print("secretEnvelope: " + str(secretEnvelope))

    # Assign cards to players
    cardDeck.dealCards(players)

    for player in players:
        printToPlayer(player, player.cards) #show them their cards
    

    # Turn
    gameWon = False
    playerCounter = 0
    turnOptions = ['Make a movement', 'Make a suggestion', 'Make an accusation', 'End turn']

    while not gameWon:
        player = players[playerCounter]
        if player.madeAccusation:
            playerCounter =  (playerCounter + 1) % len(players) #skip the player
        else:
            otherPlayers = [otherPlayer for i, otherPlayer in enumerate(players) if otherPlayer != player]

            printToPlayer(player, player.name + ", it's your turn:")
            # printToPlayer(player, "1. Make a movement")
            # printToPlayer(player, "2. Make a suggestion")
            # printToPlayer(player, "3. Make an accusation")
            # chosenOption = str(getPlayerInput(player, "Please enter the index of the desired option.")) # Didn't incorporate Exception handling here. Please only choose 1, 2, or 3
            chosenOption = selectFromList(player, turnOptions)


            if chosenOption == 'Make a movement':
                if player.madeMovement:
                    printToPlayer(player, "You already made a move during this turn.")
                else:
                    targetedPosition = [-1, -1]
                    while not gameBoard.validateMove(player.character, targetedPosition):
                        targetedPositionString = getPlayerInput(player, "Please enter a valid desired position to move your character to in the following format: row,col\n")
                        targetedPosition = targetedPositionString.split(",")
                        for axis in range(len(targetedPosition)):
                            targetedPosition[axis] = int(targetedPosition[axis])
                        
                    gameBoard.moveBoardObject(player.character, targetedPosition)
                    printAll(players, gameBoard.printBoard() + "\n")

                    player.madeMovement = True


            elif chosenOption == 'Make a suggestion':
                if player.madeSuggestion:
                    printToPlayer(player, "You already made a suggestion during this turn.")
                elif isinstance(gameBoard.getRoomByPosition(player.character.position), Hallway):
                    printToPlayer(player, "You can only make a suggestion when you are in a room.")
                else:
                    # characterCounter = 0
                    # for character in gameBoard.characters:
                    #     printToPlayer(player, character.name
                    printToPlayer(player, "Pick a character")
                    chosenChar = selectFromList(player, gameBoard.characters, 'name', False)
                    printToPlayer(player, "Pick a weapon")
                    chosenWeapon = selectFromList(player, gameBoard.weapons, 'name', False)
                    chosenRoom = gameBoard.getRoomByPosition(player.character.position)
                    suggestion = [chosenChar.name, chosenWeapon.name, chosenRoom.name]
                    

                    # move(chosenChar, chosenRoom)
                    if chosenChar not in chosenRoom.boardObjects:
                        gameBoard.moveToARoom(chosenChar, chosenRoom)
                    # move(chosenWeapon, chosenRoom)
                    if chosenWeapon not in chosenRoom.boardObjects:
                        gameBoard.moveToARoom(chosenWeapon, chosenRoom)

                    printAll(players, gameBoard.printBoard() + "\n")
                    printAll(players, player.name + " made the following suggestion: " + str(suggestion))

                    for otherPlayer in otherPlayers:
                        # Check if otherPlayer has any of the objects
                        commonObjects = []
                        for chosenObject in suggestion:
                            if chosenObject in otherPlayer.cards:
                                commonObjects.append(chosenObject)

                        if commonObjects:
                            printToPlayer(otherPlayer, player.name + " chose the following suggestion: " + str(suggestion))
                            chosenCardToShow = selectFromList(otherPlayer, commonObjects)
                            printToPlayer(player, otherPlayer.name + " shows you this card: " + chosenCardToShow)
                            break

                        printToPlayer(player, "No one could prove your suggestion was wrong!")

                    player.madeSuggestion = True

            elif chosenOption == "Make an accusation":
                chosenChar = selectFromList(player, gameBoard.characters, 'name', False)
                chosenWeapon = selectFromList(player, gameBoard.weapons, 'name', False)
                chosenRoom = selectFromList(player, gameBoard.rooms, 'name', False)
                accusation = [chosenChar.name, chosenWeapon.name, chosenRoom.name]

                if len(set(accusation) & set(secretEnvelope)) == 3:
                    printToPlayer(player, "Your accusation was correct! You won the game!! YAY!!!")
                    gameWon = True
                else:
                    printToPlayer(player, "Your accusation was incorrect! Sorry")
                    playerCounter =  (playerCounter + 1) % len(players)
                    player.madeAccusation = True
                    
                    accusationsMadeCounter = 1
                    for otherPlayer in otherPlayers:
                        if otherPlayer.madeAccusation:
                            accusationsMadeCounter += 1
                        else:
                            playerWon = otherPlayer

                    if accusationsMadeCounter >= len(players)-1:
                        printToPlayer(playerWon, "You are the last one standing. You won the game!")
                        gameWon = True



                #printToPlayer(player, "chosenChar: " + chosenChar.name)
            elif chosenOption == "End turn":
                playerCounter =  (playerCounter + 1) % len(players)
                player.refresh()

    printAll(players, "Ending game")
    # Debugging use
    # while True:
    #     if globalReply != '':
    #         print("globalReply: " + globalReply)
    #         #sys.stdout.flush()
    #         globalReply = ''
    # print "not listening anymore"
            