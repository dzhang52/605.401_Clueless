import os, sys
from PySide.QtCore import Qt, SIGNAL, SLOT, QObject
from PySide.QtGui import QPixmap, QDialog, QPushButton, QAction, QCheckBox, QComboBox, QLabel, QVBoxLayout, QGridLayout, QHBoxLayout, QDialogButtonBox
from qtpy import QtWidgets, QtGui, QtCore

'''
    comboBox = QComboBox(self)
    comboBox.addItem("1150x715")
    comboBox.addItem("1325x825")
    comboBox.addItem("1750x1100")
    comboBox.addItem("2010x1375")
    comboBox.addItem("2650x1650")
'''

class BoardGUI(QtWidgets.QWidget):

  def __init__(self):
    super(BoardGUI, self).__init__()

  def sizes(self):
    sizes = []
    self.i = 1150
    self.j = 715
    self.unitsize = (self.j/11)
    self.roomsize = (self.unitsize*3)
    self.iconsize = (2*self.unitsize/3)
    self.offsetsize = ((self.unitsize-self.iconsize)/2)
    sizes = [self.i, self.j, self.unitsize, self.roomsize, self.iconsize, self.offsetsize]
    return sizes

  def init_ui(self):
    sizeimport = self.sizes()
    self.resize(sizeimport[0], sizeimport[1])  #size of one box is 150x150pixels
    self.setWindowTitle("Clueless")
    self.setWindowIcon(QtGui.QIcon('mag.png'))
    self.set_background()
    self.sizes()
    #self.detective_notes()
    #self.boardlayout()
    #self.player_setup()
    self.show()

  def set_background(self):
    p = self.palette()
    p.setColor(self.backgroundRole(), Qt.gray)
    self.setPalette(p)

  def boardlayout(self):
    sizeimport = self.sizes()
    # These are all the rooms in column 1
    study = QtWidgets.QLabel(self)
    study.setGeometry(0, 0, sizeimport[3], sizeimport[3])
    studyImg = QPixmap(os.getcwd() + './study.png').scaled(sizeimport[3], sizeimport[3])
    study.setPixmap(studyImg)

    hallway1 = QtWidgets.QLabel(self)
    hallway1.setGeometry(sizeimport[2], 3*sizeimport[2], sizeimport[2], sizeimport[2])
    hallwayImg = QPixmap(os.getcwd() + './hallway_vertical.png').scaled(sizeimport[2], sizeimport[2])
    hallway1.setPixmap(hallwayImg)

    library = QtWidgets.QLabel(self)
    library.setGeometry(0, 4*sizeimport[2], sizeimport[3], sizeimport[3])
    libraryImg = QPixmap(os.getcwd() + './library.png').scaled(sizeimport[3], sizeimport[3])
    library.setPixmap(libraryImg)

    hallway2 = QtWidgets.QLabel(self)
    hallway2.setGeometry(sizeimport[2], 7*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway2.setPixmap(hallwayImg)

    conservatory = QtWidgets.QLabel(self)
    conservatory.setGeometry(0, 8*sizeimport[2], sizeimport[3], sizeimport[3])
    conservatoryImg = QPixmap(os.getcwd() + './conservatory.png').scaled(sizeimport[3], sizeimport[3])
    conservatory.setPixmap(conservatoryImg)

    # These are all the vertical hallways between Column 1 & 2
    hallway3 = QtWidgets.QLabel(self)
    hallway3.setGeometry(3*sizeimport[2], sizeimport[2], sizeimport[2], sizeimport[2])
    hallwayImg_v = QPixmap(os.getcwd() + './hallway_horizontal.png').scaled(sizeimport[2], sizeimport[2])
    hallway3.setPixmap(hallwayImg_v)

    hallway4 = QtWidgets.QLabel(self)
    hallway4.setGeometry(3*sizeimport[2], 5*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway4.setPixmap(hallwayImg_v)

    hallway5 = QtWidgets.QLabel(self)
    hallway5.setGeometry(3*sizeimport[2], 9*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway5.setPixmap(hallwayImg_v)

    # These are all the rooms in column 2
    ball = QtWidgets.QLabel(self)
    ball.setGeometry(4*sizeimport[2], 0, sizeimport[3], sizeimport[3])
    ballImg = QPixmap(os.getcwd() + './ballroom.png').scaled(sizeimport[3], sizeimport[3])
    ball.setPixmap(ballImg)

    hallway6 = QtWidgets.QLabel(self)
    hallway6.setGeometry(5*sizeimport[2], 3*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway6.setPixmap(hallwayImg)

    billiards = QtWidgets.QLabel(self)
    billiards.setGeometry(4*sizeimport[2], 4*sizeimport[2], sizeimport[3], sizeimport[3])
    billiardsImg = QPixmap(os.getcwd() + './billiards_room.png').scaled(sizeimport[3], sizeimport[3])
    billiards.setPixmap(billiardsImg)

    hallway7 = QtWidgets.QLabel(self)
    hallway7.setGeometry(5*sizeimport[2], 7*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway7.setPixmap(hallwayImg)

    hall = QtWidgets.QLabel(self)
    hall.setGeometry(4*sizeimport[2], 8*sizeimport[2], sizeimport[3], sizeimport[3])
    hallImg = QPixmap(os.getcwd() + './hall.png').scaled(sizeimport[3], sizeimport[3])
    hall.setPixmap(hallImg)

    # These are all the halls between column 2 & 3
    hallway8 = QtWidgets.QLabel(self)
    hallway8.setGeometry(7*sizeimport[2], sizeimport[2], sizeimport[2], sizeimport[2])
    hallway8.setPixmap(hallwayImg_v)

    hallway9 = QtWidgets.QLabel(self)
    hallway9.setGeometry(7*sizeimport[2], 5*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway9.setPixmap(hallwayImg_v)

    hallway10 = QtWidgets.QLabel(self)
    hallway10.setGeometry(7*sizeimport[2], 9*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway10.setPixmap(hallwayImg_v)

    # These are all the rooms in column 3
    lounge = QtWidgets.QLabel(self)
    lounge.setGeometry(8*sizeimport[2], 0, sizeimport[3], sizeimport[3])
    loungeImg = QPixmap(os.getcwd() + './lounge.png').scaled(sizeimport[3], sizeimport[3])
    lounge.setPixmap(loungeImg)

    hallway11 = QtWidgets.QLabel(self)
    hallway11.setGeometry(9*sizeimport[2], 3*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway11.setPixmap(hallwayImg)

    dining = QtWidgets.QLabel(self)
    dining.setGeometry(8*sizeimport[2], 4*sizeimport[2], sizeimport[3], sizeimport[3])
    diningImg = QPixmap(os.getcwd() + './dining_room.png').scaled(sizeimport[3], sizeimport[3])
    dining.setPixmap(diningImg)

    hallway12 = QtWidgets.QLabel(self)
    hallway12.setGeometry(9*sizeimport[2], 7*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway12.setPixmap(hallwayImg)

    kitchen = QtWidgets.QLabel(self)
    kitchen.setGeometry(8*sizeimport[2], 8*sizeimport[2], sizeimport[3], sizeimport[3])
    kitchenImg = QPixmap(os.getcwd() + './kitchen.png').scaled(sizeimport[3], sizeimport[3])
    kitchen.setPixmap(kitchenImg)

  def player_setup(self, name, j, i):
    sizeimport = self.sizes()
    p = [(0*sizeimport[2]+sizeimport[5]), (1*sizeimport[2]+sizeimport[5]), (2*sizeimport[2]+sizeimport[5]), (3*sizeimport[2]+sizeimport[5]), (4*sizeimport[2]+sizeimport[5]), (5*sizeimport[2]+sizeimport[5]), (6*sizeimport[2]+sizeimport[5]), (7*sizeimport[2]+sizeimport[5]), (8*sizeimport[2]+sizeimport[5]), (9*sizeimport[2]+sizeimport[5]), (10*sizeimport[2]+sizeimport[5])]

    if name == "Miss Scarlet":
      scarlet = QtWidgets.QLabel(self)
      redIcon = QPixmap(os.getcwd() + './red.png').scaledToHeight(sizeimport[4])
      scarlet.move(p[i], p[j])
      scarlet.setPixmap(redIcon)
    if name == "Colonel Mustard":
      mustard = QtWidgets.QLabel(self)
      brownIcon = QPixmap(os.getcwd() + './brown.png').scaledToHeight(sizeimport[4])
      mustard.move(p[i], p[j])
      mustard.setPixmap(brownIcon)
    if name == "Mrs. White":
      white = QtWidgets.QLabel(self)
      greyIcon = QPixmap(os.getcwd() + './grey.png').scaledToHeight(sizeimport[4])
      white.move(p[i], p[j])
      white.setPixmap(greyIcon)
    if name == "Mr. Green":
      green = QtWidgets.QLabel(self)
      greenIcon = QPixmap(os.getcwd() + './green.png').scaledToHeight(sizeimport[4])
      green.move(p[i], p[j])
      green.setPixmap(greenIcon)
    if name == "Mrs. Peacock":
      peacock = QtWidgets.QLabel(self)
      blueIcon = QPixmap(os.getcwd() + './blue.ico').scaledToHeight(sizeimport[4])
      peacock.move(p[i], p[j])
      peacock.setPixmap(blueIcon)
    if name == "Professor Plum":
      plum = QtWidgets.QLabel(self)
      purpleIcon = QPixmap(os.getcwd() + './purple.png').scaledToHeight(sizeimport[4])
      plum.move(p[i], p[j])
      plum.setPixmap(purpleIcon)

  def weapon_setup(self, name, j, i):
    sizeimport = self.sizes()
    p = [(0*sizeimport[2]), (1*sizeimport[2]), (2*sizeimport[2]), (3*sizeimport[2]), (4*sizeimport[2]), (5*sizeimport[2]), (6*sizeimport[2]), (7*sizeimport[2]), (8*sizeimport[2]), (9*sizeimport[2]), (10*sizeimport[2])]

    if name == "Wrench":
      scarlet = QtWidgets.QLabel(self)
      redIcon = QPixmap(os.getcwd() + './wrench.ico').scaledToHeight(sizeimport[4])
      scarlet.move(p[i], p[j])
      scarlet.setPixmap(redIcon)
    if name == "Rope":
      mustard = QtWidgets.QLabel(self)
      brownIcon = QPixmap(os.getcwd() + './Rope.ico').scaledToHeight(sizeimport[4])
      mustard.move(p[i], p[j])
      mustard.setPixmap(brownIcon)
    if name == "Revolver":
      white = QtWidgets.QLabel(self)
      greyIcon = QPixmap(os.getcwd() + './revolver.ico').scaledToHeight(sizeimport[4])
      white.move(p[i], p[j])
      white.setPixmap(greyIcon)
    if name == "knife":
      green = QtWidgets.QLabel(self)
      greenIcon = QPixmap(os.getcwd() + './knife.ico').scaledToHeight(sizeimport[4])
      green.move(p[i], p[j])
      green.setPixmap(greenIcon)
    if name == "Candlestick":
      peacock = QtWidgets.QLabel(self)
      blueIcon = QPixmap(os.getcwd() + './candlestick.ico').scaledToHeight(sizeimport[4])
      peacock.move(p[i], p[j])
      peacock.setPixmap(blueIcon)
    if name == "Lead Pipe":
      plum = QtWidgets.QLabel(self)
      purpleIcon = QPixmap(os.getcwd() + './pipe.ico').scaledToHeight(sizeimport[4])
      plum.move(p[i], p[j])
      plum.setPixmap(purpleIcon)

  def detective_notes(self):
    sizeimport = self.sizes()
    notes = QtWidgets.QWidget(self)
    suspects = QtWidgets.QWidget(self)
    weapons = QtWidgets.QWidget(self)
    rooms = QtWidgets.QWidget(self)
    notes.setGeometry((sizeimport[1]), 0, (sizeimport[0]-sizeimport[1]), sizeimport[1])

    Title1 = QtWidgets.QLabel(self)
    Title1.setStyleSheet(" font-size: 30px; font-style: bold; qproperty-alignment: AlignCenter; font-family: Times New Roman;")
    Title2 = QtWidgets.QLabel(self)
    Title2.setStyleSheet(" font-size: 20px; font-style: bold; qproperty-alignment: AlignLeft; font-family: Times New Roman;")
    Title3 = QtWidgets.QLabel(self)
    Title3.setStyleSheet(" font-size: 20px; font-style: bold; qproperty-alignment: AlignLeft; font-family: Times New Roman;")
    Title4 = QtWidgets.QLabel(self)
    Title4.setStyleSheet(" font-size: 20px; font-style: bold; qproperty-alignment: AlignLeft; font-family: Times New Roman;")

    Suspect1 = QtWidgets.QLabel(self)
    Suspect2 = QtWidgets.QLabel(self)
    Suspect3 = QtWidgets.QLabel(self)
    Suspect4 = QtWidgets.QLabel(self)
    Suspect5 = QtWidgets.QLabel(self)
    Suspect6 = QtWidgets.QLabel(self)

    Weapon1 = QtWidgets.QLabel(self)
    Weapon2 = QtWidgets.QLabel(self)
    Weapon3 = QtWidgets.QLabel(self)
    Weapon4 = QtWidgets.QLabel(self)
    Weapon5 = QtWidgets.QLabel(self)
    Weapon6 = QtWidgets.QLabel(self)

    Room1 = QtWidgets.QLabel(self)
    Room2 = QtWidgets.QLabel(self)
    Room3 = QtWidgets.QLabel(self)
    Room4 = QtWidgets.QLabel(self)
    Room5 = QtWidgets.QLabel(self)
    Room6 = QtWidgets.QLabel(self)
    Room7 = QtWidgets.QLabel(self)
    Room8 = QtWidgets.QLabel(self)
    Room9 = QtWidgets.QLabel(self)

    TextEdit = QtWidgets.QTextEdit(self)

    Title1.setText("Detective Notes")
    Title2.setText("Suspects")
    Title3.setText("Location")
    Title4.setText("Weapon")

    Suspect1.setText("test1")
    Suspect2.setText("test2")
    Suspect3.setText("test3")
    Suspect4.setText("test4")
    Suspect5.setText("test5")
    Suspect6.setText("test6")

    Weapon1.setText("test1")
    Weapon2.setText("test2")
    Weapon3.setText("test3")
    Weapon4.setText("test4")
    Weapon5.setText("test5")
    Weapon6.setText("test6")

    Room1.setText("Test1")
    Room2.setText("Test2")
    Room3.setText("Test3")
    Room4.setText("Test4")
    Room5.setText("Test5")
    Room6.setText("Test6")
    Room7.setText("Test7")
    Room8.setText("Test8")
    Room9.setText("Test9")


    suspect_grid = QtWidgets.QGridLayout()
    suspect_grid.addWidget(Suspect1, 0, 0)
    suspect_grid.addWidget(Suspect2, 1, 0)
    suspect_grid.addWidget(Suspect3, 2, 0)
    suspect_grid.addWidget(Suspect4, 0, 1)
    suspect_grid.addWidget(Suspect5, 1, 1)
    suspect_grid.addWidget(Suspect6, 2, 1)

    suspects.setLayout(suspect_grid)

    weapon_grid = QtWidgets.QGridLayout()
    weapon_grid.addWidget(Weapon1, 0, 0)
    weapon_grid.addWidget(Weapon2, 1, 0)
    weapon_grid.addWidget(Weapon3, 2, 0)
    weapon_grid.addWidget(Weapon4, 0, 1)
    weapon_grid.addWidget(Weapon5, 1, 1)
    weapon_grid.addWidget(Weapon6, 2, 1)

    weapons.setLayout(weapon_grid)

    room_grid = QtWidgets.QGridLayout()
    room_grid.addWidget(Room1, 0, 0)
    room_grid.addWidget(Room2, 1, 0)
    room_grid.addWidget(Room3, 2, 0)
    room_grid.addWidget(Room4, 0, 1)
    room_grid.addWidget(Room5, 1, 1)
    room_grid.addWidget(Room6, 2, 1)
    room_grid.addWidget(Room7, 0, 2)
    room_grid.addWidget(Room8, 1, 2)
    room_grid.addWidget(Room9, 2, 2)

    rooms.setLayout(room_grid)

    vbox = QtWidgets.QVBoxLayout()
    vbox.addWidget(Title1)
    vbox.addWidget(Title2)
    vbox.addWidget(suspects)
    vbox.addWidget(Title3)
    vbox.addWidget(rooms)
    vbox.addWidget(Title4)
    vbox.addWidget(weapons)
    vbox.addWidget(TextEdit)

    notes.setLayout(vbox)

