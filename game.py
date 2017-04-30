from random import shuffle

# Wrapper class to add asSymbol method for strings
class String(str):
    def asSymbol(self):
        return self

class Direction(object):
    left = 0
    up = 1
    right = 2
    down = 3

    @staticmethod
    def opposite(position):
        base = int('11', 2)
        oppositeDir = (position + 2) & base

        #print "oppositeDir: " + str(oppositeDir)
        return oppositeDir

class BoardSpace(object):

    #length = 0
    #width = 0
    #connectedTo = [None, None, None, None]

    def __init__(self, length, width, position):
        #self.boardPosition = [0,0]
        self.length = length
        self.width = width
        self.position = position
        self.connectedTo = [None, None, None, None] #[left, up, right, down]
        self.boardObjects = []
        #print "in boardspace"

    def addConnection(self, position, connection):
        self.connectedTo[position] = connection
        connection.connectedTo[Direction.opposite(position)] = self

    def asSymbol(self):
        return "x"

    def addBoardObject(self, boardObject):
        self.boardObjects.append(boardObject)

    def delBoardObject(self, boardObject):
        self.boardObjects.remove(boardObject)


class Room(BoardSpace):
    #length = 3
    #width = 3
    #connectedTo = [None, None, None, None]

    def __init__(self, position): #connections is an array
        #print "in Room"
        super(Room,self).__init__(3,3,position)
        #print "Room length: " + str(self.length)

    def initializeMatrix(self):
        self.matrix = [[ self for x in range(self.width)] for y in range(self.length) ]

    # def print(self):
    #     for i in range(self.length):
    #         for j in range(self.width):
    #             print "+"

    
class Hallway(BoardSpace):
    
    def __init__(self, position): #connections is an array
        #print "in Hallway"
        super(Hallway,self).__init__(1,1,position)

    def initializeMatrix(self):
        self.matrix = [[String(' ')]]
        if self.connectedTo[Direction.right] == None:
            self.matrix[0] += [self] + [String(' ')]
        elif self.connectedTo[Direction.up] == None:
            self.matrix += [[self]] + [[String(' ')]]


        #return returnMatrix

    # def print(self):
    #     for connection in connectedTo:
    #         if connection == None:
    #             print " "

class BoardObject(object):
    def __init__(self, name, symbol, position=None):
        self.name = name
        self.symbol = symbol
        self.position = position

    def setPosition(self, position):
        self.position = position

    def asSymbol(self):
        return self.symbol

    def getName(self):
        return self.name

class Character(BoardObject):
    pass

class Weapon(BoardObject):
    pass

class GameBoard(object):

    # def __init__(self):
    #     self.sideLength = 11
    #     self.board = [[ ' ' for x in range(self.sideLength)] for y in range(self.sideLength) ]

    #     self.testB01 = [[ 'x' for x in range(3)] for y in range(3) ]
    #     self.testB02 = [[ 'y' for x in range(3)] for y in range(1) ]

    #     self.testA = self.testB01 + self.testB02
    #     print "in gameboard"
    #     print self.testB02
    #     print self.testA
    #     self.printBoard(self.testA)

    # def test(self):
    #     for row in self.board:
    #         for item in row:
    #             print item
    
    def printBoard(self):
        return '\n'.join([''.join(['{:2}'.format(item.asSymbol()) for item in row]) for row in self.board])

    def concatenateMatrices(self, *matrices):
        # rowNum = 0
        # while rowNum < len(attachment):
        #     try:
        #         self.board[rowNum] += attachment[rowNum]
        #     except IndexError:
        #         self.board += attachment[rowNum:]
        
        returnMatrix = [[] for i in range(len(matrices[0]))]
        for matrix in matrices:
            for rowNum in range(len(matrix)):
                returnMatrix[rowNum] += matrix[rowNum]

        return returnMatrix


    def initialize(self):
        mustard = Character("Colonel Mustard", "M")
        scarle = Character("Miss Scarle", "S")
        plum = Character("Professor Plum", "P")
        green = Character("Mr. Green", "G")
        white = Character("Mrs. White", "W")
        peacock = Character("Mrs. Peacock", "B")

        self.characters = [mustard, scarle, plum, green, white, peacock]

        rope = Weapon("Rope", "R")
        pipe = Weapon("Lead Pipe", "L")
        knife = Weapon("knife", "K")
        wrench = Weapon("Wrench", "H")
        candlestick = Weapon("Candlestick", "C")
        revolver = Weapon("Revolver", "R")

        self.weapons = [rope, pipe, knife, wrench, candlestick, revolver]

        study = Room([1,1])
        hall = Room([1,5])
        library = Room([5,1])
        lounge = Room([1,9])
        billiardRoom = Room([5,5])
        diningRoom = Room([5,9])
        conservatory = Room([9,1])
        ballRoom = Room([9,5])
        kitchen = Room([9,9])

        self.rooms = [study, hall, library, lounge, billiardRoom, diningRoom, conservatory, ballRoom, kitchen]

        hallway1 = Hallway([1,3])
        hallway2 = Hallway([1,7])
        hallway3 = Hallway([3,1])
        hallway4 = Hallway([3,5])
        hallway5 = Hallway([3,9])
        hallway6 = Hallway([5,3])
        hallway7 = Hallway([5,7])
        hallway8 = Hallway([7,1])
        hallway9 = Hallway([7,5])
        hallway10 = Hallway([7,9])
        hallway11 = Hallway([9,3])
        hallway12 = Hallway([9,7])

        self.hallways = [hallway1, hallway2, hallway3, hallway4, hallway5, hallway6, hallway7, hallway8 , hallway9, hallway10, hallway11, hallway12]

        study.addConnection(Direction.right, hallway1)
        study.addConnection(Direction.down, hallway3)

        hall.addConnection(Direction.left, hallway1)
        hall.addConnection(Direction.right, hallway2)
        hall.addConnection(Direction.down, hallway4)
        
        lounge.addConnection(Direction.left, hallway2)
        lounge.addConnection(Direction.down, hallway5)

        library.addConnection(Direction.up, hallway3)
        library.addConnection(Direction.right, hallway6)
        library.addConnection(Direction.down, hallway8)

        billiardRoom.addConnection(Direction.left, hallway6)
        billiardRoom.addConnection(Direction.up, hallway4)
        billiardRoom.addConnection(Direction.right, hallway7)
        billiardRoom.addConnection(Direction.down,hallway9)

        diningRoom.addConnection(Direction.up, hallway5)
        diningRoom.addConnection(Direction.left, hallway7)
        diningRoom.addConnection(Direction.down, hallway10)

        conservatory.addConnection(Direction.up, hallway8)
        conservatory.addConnection(Direction.right, hallway11)

        ballRoom.addConnection(Direction.left, hallway11)
        ballRoom.addConnection(Direction.up, hallway9)
        ballRoom.addConnection(Direction.right, hallway12)

        kitchen.addConnection(Direction.left, hallway12)
        kitchen.addConnection(Direction.up, hallway10)

        for room in self.rooms:
            room.initializeMatrix()

        for hallway in self.hallways:
            hallway.initializeMatrix()

        self.board = self.concatenateMatrices(study.matrix, hallway1.matrix, hall.matrix, hallway2.matrix, lounge.matrix) + \
                     self.concatenateMatrices(hallway3.matrix, [[String(' ')]], hallway4.matrix, [[String(' ')]], hallway5.matrix) + \
                     self.concatenateMatrices(library.matrix, hallway6.matrix, billiardRoom.matrix, hallway7.matrix, diningRoom.matrix) + \
                     self.concatenateMatrices(hallway8.matrix, [[String(' ')]], hallway9.matrix, [[String(' ')]], hallway10.matrix) + \
                     self.concatenateMatrices(conservatory.matrix, hallway11.matrix, ballRoom.matrix, hallway12.matrix, kitchen.matrix)
        
        self.discardedObj = {}

        #self.board[0][2] = scarle
        self.addBoardObject(mustard, [3,9])
        self.addBoardObject(scarle, [1,7])
        self.addBoardObject(plum, [3,1])
        self.addBoardObject(peacock, [7,1])
        self.addBoardObject(green, [9,3])
        self.addBoardObject(white, [9,7])

        randomRooms = self.randomRooms()
        for WeaponIndex in range(len(self.weapons)):
            self.addBoardObject(self.weapons[WeaponIndex], randomRooms[WeaponIndex].position)

    def randomRooms(self):
        randomRooms = self.rooms
        shuffle(randomRooms)
        return randomRooms

    def addBoardObject(self, boardObject, position):
        positionString = str(position[0]) + "," + str(position[1])
        originalObj = self.board[position[0]][position[1]]
        originalObj.addBoardObject(boardObject)
        self.discardedObj[positionString] = originalObj
        self.board[position[0]][position[1]] = boardObject
        boardObject.setPosition(position)

    def delBoardObject(self, boardObject):
        position = boardObject.position
        positionString = str(position[0]) + "," + str(position[1])
        originalObj = self.discardedObj[positionString]
        originalObj.delBoardObject(boardObject)
        self.board[position[0]][position[1]] = originalObj
        del self.discardedObj[positionString]

    def translatePosition(self,position):
        if (position[0]==3 or position[0]==7):
            return [1,0]
        elif (position[0]>=4 and position[0]<=6):
            position[0]-=4
        elif (position[0]>=8 and position[0]<=10):
            position[0]-=8
        
        if (position[1]==3 or position[1]==7):
            return [0,1]
        elif (position[1]>=4 and position[1]<=6):
            position[1]-=4
        elif (position[1]>=8 and position[1]<=10):
            position[1]-=8

        return position
        
        

if __name__ == '__main__':
    gameBoard = GameBoard()
    gameBoard.initialize()
    print gameBoard.printBoard()
    print gameBoard.discardedObj
    print "discardedObj length: " + str(len(gameBoard.discardedObj))
    print gameBoard.hallways[2].boardObjects

    charEx = Character("Colonel Mustant", "M")
    print charEx.asSymbol()
    #gameBoard.test()
    #roomEx = Room()
    #roomBoard = roomEx.asSymbol()
    #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in roomBoard]))

    #hallwayEx = Hallway()
    #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in hallwayEx.asSymbol()]))