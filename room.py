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

    def __init__(self, length, width):
        #self.boardPosition = [0,0]
        self.length = length
        self.width = width
        self.connectedTo = [None, None, None, None] #[left, up, right, down]
        #print "in boardspace"

    def addConnection(self, position, connection):
        self.connectedTo[position] = connection
        connection.connectedTo[Direction.opposite(position)] = self

    def asSymbol(self):
        return "x"
        


class Room(BoardSpace):
    #length = 3
    #width = 3
    #connectedTo = [None, None, None, None]

    def __init__(self): #connections is an array
        #print "in Room"
        super(Room,self).__init__(3,3)
        #print "Room length: " + str(self.length)

    def asMatrix(self):
        return [[ self for x in range(self.width)] for y in range(self.length) ]

    # def print(self):
    #     for i in range(self.length):
    #         for j in range(self.width):
    #             print "+"

    
class Hallway(BoardSpace):
    
    def __init__(self): #connections is an array
        #print "in Hallway"
        super(Hallway,self).__init__(1,3)
        #print "Hallway length: " + str(self.length)

    def asMatrix(self):
        returnMatrix = [[String(' ')]]
        if self.connectedTo[Direction.right] == None:
            returnMatrix[0] += [self] + [String(' ')]
        elif self.connectedTo[Direction.up] == None:
            returnMatrix += [[self]] + [[String(' ')]]

        return returnMatrix

    # def print(self):
    #     for connection in connectedTo:
    #         if connection == None:
    #             print " "

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
        print('\n'.join([''.join(['{:2}'.format(item.asSymbol()) for item in row]) for row in self.board]))

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
        study = Room()
        hall = Room()
        library = Room()
        lounge = Room()
        billiardRoom = Room()
        diningRoom = Room()
        conservatory = Room()
        ballRoom = Room()
        kitchen = Room()

        hallway1 = Hallway()
        hallway2 = Hallway()
        hallway3 = Hallway()
        hallway4 = Hallway()
        hallway5 = Hallway()
        hallway6 = Hallway()
        hallway7 = Hallway()
        hallway8 = Hallway()
        hallway9 = Hallway()
        hallway10 = Hallway()
        hallway11 = Hallway()
        hallway12 = Hallway()

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

        self.board = self.concatenateMatrices(study.asMatrix(), hallway1.asMatrix(), hall.asMatrix(), hallway2.asMatrix(), lounge.asMatrix()) + \
                     self.concatenateMatrices(hallway3.asMatrix(), [[String(' ')]], hallway4.asMatrix(), [[String(' ')]], hallway5.asMatrix()) + \
                     self.concatenateMatrices(library.asMatrix(), hallway6.asMatrix(), billiardRoom.asMatrix(), hallway7.asMatrix(), diningRoom.asMatrix()) + \
                     self.concatenateMatrices(hallway8.asMatrix(), [[String(' ')]], hallway9.asMatrix(), [[String(' ')]], hallway10.asMatrix()) + \
                     self.concatenateMatrices(conservatory.asMatrix(), hallway11.asMatrix(), ballRoom.asMatrix(), hallway12.asMatrix(), kitchen.asMatrix())

if __name__ == '__main__':
    gameBoard = GameBoard()
    gameBoard.initialize()
    gameBoard.printBoard()
    #gameBoard.test()
    #roomEx = Room()
    #roomBoard = roomEx.asSymbol()
    #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in roomBoard]))

    #hallwayEx = Hallway()
    #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in hallwayEx.asSymbol()]))