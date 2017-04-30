from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QGridLayout, QSizePolicy, QLabel
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QSize, QPoint
import sys, os


class BoardGUI(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()
    self.start_game()

#I want to use this to check if there is an on going game first
  def start_game(self):
    startGame = QMessageBox.question(self, 'Message', "Do you Want to Play Clueless?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if startGame == QMessageBox.Yes:
      self.init_ui()
    else:
      quit

  def init_ui(self):
    self.resize(2650, 1650)  #size of one box is 150x150pixels
    self.setWindowTitle("Clueless")
    self.setWindowIcon(QtGui.QIcon('mag.png'))
    self.set_background()
    self.room_setup()
    self.player_setup()
    self.show()

  def room_setup(self):
#These are all the rooms in column 1
    study = QtWidgets.QLabel(self)
    study.setGeometry(0, 0, 450, 450)
    studyImg = QPixmap(os.getcwd() + './study.png').scaled(450, 450)
    study.setPixmap(studyImg)

    hallway1 = QtWidgets.QLabel(self)
    hallway1.setGeometry(150, 450, 150, 150)
    hallwayImg = QPixmap(os.getcwd() + './hallway_vertical.png').scaled(150, 150)
    hallway1.setPixmap(hallwayImg)

    library = QtWidgets.QLabel(self)
    library.setGeometry(0, 600, 450, 450)
    libraryImg = QPixmap(os.getcwd() + './library.png').scaled(450, 450)
    library.setPixmap(libraryImg)

    hallway2 = QtWidgets.QLabel(self)
    hallway2.setGeometry(150, 1050, 150, 150)
    hallway2.setPixmap(hallwayImg)

    conservatory = QtWidgets.QLabel(self)
    conservatory.setGeometry(0, 1200, 450, 450)
    conservatoryImg = QPixmap(os.getcwd() + './conservatory.png').scaled(450, 450)
    conservatory.setPixmap(conservatoryImg)

#These are all the vertical hallways between Column 1 & 2
    hallway3 = QtWidgets.QLabel(self)
    hallway3.setGeometry(450, 150, 150, 150)
    hallwayImg_v = QPixmap(os.getcwd() + './hallway_horizontal.png').scaled(150, 150)
    hallway3.setPixmap(hallwayImg_v)

    hallway4 = QtWidgets.QLabel(self)
    hallway4.setGeometry(450, 750, 150, 150)
    hallway4.setPixmap(hallwayImg_v)

    hallway5 = QtWidgets.QLabel(self)
    hallway5.setGeometry(450, 1350, 150, 150)
    hallway5.setPixmap(hallwayImg_v)

#These are all the rooms in column 2
    ball = QtWidgets.QLabel(self)
    ball.setGeometry(600, 0, 450, 450)
    ballImg = QPixmap(os.getcwd() + './ballroom.png').scaled(450, 450)
    ball.setPixmap(ballImg)

    hallway6 = QtWidgets.QLabel(self)
    hallway6.setGeometry(750, 450, 150, 150)
    hallway6.setPixmap(hallwayImg)

    billiards = QtWidgets.QLabel(self)
    billiards.setGeometry(600, 600, 450, 450)
    billiardsImg = QPixmap(os.getcwd() + './billiards_room.png').scaled(450, 450)
    billiards.setPixmap(billiardsImg)

    hallway7 = QtWidgets.QLabel(self)
    hallway7.setGeometry(750, 1050, 150, 150)
    hallway7.setPixmap(hallwayImg)

    hall = QtWidgets.QLabel(self)
    hall.setGeometry(600, 1200, 450, 450)
    hallImg = QPixmap(os.getcwd() + './hall.png').scaled(450, 450)
    hall.setPixmap(hallImg)


#These are all the halls between column 2 & 3
    hallway8 = QtWidgets.QLabel(self)
    hallway8.setGeometry(1050, 150, 150, 150)
    hallway8.setPixmap(hallwayImg_v)

    hallway9 = QtWidgets.QLabel(self)
    hallway9.setGeometry(1050, 750, 150, 150)
    hallway9.setPixmap(hallwayImg_v)

    hallway10 = QtWidgets.QLabel(self)
    hallway10.setGeometry(1050, 1350, 150, 150)
    hallway10.setPixmap(hallwayImg_v)

#These are all the rooms in column 3
    lounge = QtWidgets.QLabel(self)
    lounge.setGeometry(1200, 0, 450, 450)
    loungeImg = QPixmap(os.getcwd() + './lounge.png').scaled(450, 450)
    lounge.setPixmap(loungeImg)

    hallway11 = QtWidgets.QLabel(self)
    hallway11.setGeometry(1350, 450, 150, 150)
    hallway11.setPixmap(hallwayImg)


    dining = QtWidgets.QLabel(self)
    dining.setGeometry(1200, 600, 450, 450)
    diningImg = QPixmap(os.getcwd() + './dining_room.png').scaled(450, 450)
    dining.setPixmap(diningImg)

    hallway12 = QtWidgets.QLabel(self)
    hallway12.setGeometry(1350, 1050, 150, 150)
    hallway12.setPixmap(hallwayImg)

    kitchen = QtWidgets.QLabel(self)
    kitchen.setGeometry(1200, 1200, 450, 450)
    kitchenImg = QPixmap(os.getcwd() + './kitchen.png').scaled(450, 450)
    kitchen.setPixmap(kitchenImg)

  def player_setup(self):

    isScarlet = True
    isMustard = True
    isWhite = True
    isGreen = True
    isPeacock = True
    isPlum = True

    if isScarlet == True:
      scarlet = QtWidgets.QLabel(self)
      redIcon = QPixmap(os.getcwd() + './red.png').scaledToHeight(100)
      scarlet.move(1075, 175)
      scarlet.setPixmap(redIcon)
    if isMustard == True:
      mustard = QtWidgets.QLabel(self)
      brownIcon = QPixmap(os.getcwd() + './brown.png').scaledToHeight(100)
      mustard.move(1375, 475)
      mustard.setPixmap(brownIcon)
    if isWhite == True:
      white = QtWidgets.QLabel(self)
      greyIcon = QPixmap(os.getcwd() + './grey.png').scaledToHeight(100)
      white.move(1075, 1375)
      white.setPixmap(greyIcon)
    if isGreen == True:
      green = QtWidgets.QLabel(self)
      greenIcon = QPixmap(os.getcwd() + './green.png').scaledToHeight(100)
      green.move(475, 1375)
      green.setPixmap(greenIcon)
    if isPeacock == True:
      peacock = QtWidgets.QLabel(self)
      blueIcon = QPixmap(os.getcwd() + './blue.ico').scaledToHeight(100)
      peacock.move(175, 1075)
      peacock.setPixmap(blueIcon)
    if isPlum == True:
      plum = QtWidgets.QLabel(self)
      purpleIcon = QPixmap(os.getcwd() + './purple.png').scaledToHeight(100)
      plum.move(175, 475)
      plum.setPixmap(purpleIcon)


  def set_background(self):
    p = self.palette()
    p.setColor(self.backgroundRole(), Qt.lightGray)
    self.setPalette(p)

if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  game = BoardGUI()
  sys.exit(app.exec_())


  # lbl0.move(50, 50)
  # lbl1.move(100, 100)
  # lbl2.move(150, 150)
  # lbl3.move(150, 150)

  # self.move(300, 200)


