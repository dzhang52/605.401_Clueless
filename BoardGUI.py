import os, sys

from PySide.QtGui import *


class BoardGUI(QWidget):

  def __init__(self):
    super(BoardGUI, self).__init__()
    self.i = 2000
    self.j = 2000
    self.setMouseTracking(True)

  def resolution(self, i, j):
    self.i = i
    self.j = j

  def sizes(self):

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
    self.setWindowIcon(QIcon('mag.png'))
    self.detective_notes()

    self.boardlayout()

    #self.player_setup()
    self.show()



  #def set_background(self):
  #  p = self.palette()
  #  p.setColor(self.backgroundRole(), Qt.gray)
  #  self.setPalette(p)

  def boardlayout(self):
    sizeimport = self.sizes()

    # These are all the rooms in column 1
    study = QLabel(self)
    study.setGeometry(0, 0, sizeimport[3], sizeimport[3])
    studyImg = QPixmap(os.getcwd() + './Rooms/study.png').scaled(sizeimport[3], sizeimport[3])
    study.setPixmap(studyImg)
    study.setStyleSheet("QLabel::item:hover{background-color:#999966;}")

    hallway1 = QLabel(self)
    hallway1.setGeometry(sizeimport[2], 3*sizeimport[2], sizeimport[2], sizeimport[2])
    hallwayImg = QPixmap(os.getcwd() + './Rooms/hallway_vertical.png').scaled(sizeimport[2], sizeimport[2])
    hallway1.setPixmap(hallwayImg)

    library = QLabel(self)
    library.setGeometry(0, 4*sizeimport[2], sizeimport[3], sizeimport[3])
    libraryImg = QPixmap(os.getcwd() + './Rooms/library.png').scaled(sizeimport[3], sizeimport[3])
    library.setPixmap(libraryImg)

    hallway2 = QLabel(self)
    hallway2.setGeometry(sizeimport[2], 7*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway2.setPixmap(hallwayImg)

    conservatory = QLabel(self)
    conservatory.setGeometry(0, 8*sizeimport[2], sizeimport[3], sizeimport[3])
    conservatoryImg = QPixmap(os.getcwd() + './Rooms/conservatory.png').scaled(sizeimport[3], sizeimport[3])
    conservatory.setPixmap(conservatoryImg)

    # These are all the vertical hallways between Column 1 & 2
    hallway3 = QLabel(self)
    hallway3.setGeometry(3*sizeimport[2], sizeimport[2], sizeimport[2], sizeimport[2])
    hallwayImg_v = QPixmap(os.getcwd() + './Rooms/hallway_horizontal.png').scaled(sizeimport[2], sizeimport[2])
    hallway3.setPixmap(hallwayImg_v)

    hallway4 = QLabel(self)
    hallway4.setGeometry(3*sizeimport[2], 5*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway4.setPixmap(hallwayImg_v)

    hallway5 = QLabel(self)
    hallway5.setGeometry(3*sizeimport[2], 9*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway5.setPixmap(hallwayImg_v)

    # These are all the rooms in column 2
    ball = QLabel(self)
    ball.setGeometry(4*sizeimport[2], 0, sizeimport[3], sizeimport[3])
    ballImg = QPixmap(os.getcwd() + './Rooms/ballroom.png').scaled(sizeimport[3], sizeimport[3])
    ball.setPixmap(ballImg)

    hallway6 = QLabel(self)
    hallway6.setGeometry(5*sizeimport[2], 3*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway6.setPixmap(hallwayImg)

    billiards = QLabel(self)
    billiards.setGeometry(4*sizeimport[2], 4*sizeimport[2], sizeimport[3], sizeimport[3])
    billiardsImg = QPixmap(os.getcwd() + './Rooms/billiards_room.png').scaled(sizeimport[3], sizeimport[3])
    billiards.setPixmap(billiardsImg)

    hallway7 = QLabel(self)
    hallway7.setGeometry(5*sizeimport[2], 7*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway7.setPixmap(hallwayImg)

    hall = QLabel(self)
    hall.setGeometry(4*sizeimport[2], 8*sizeimport[2], sizeimport[3], sizeimport[3])
    hallImg = QPixmap(os.getcwd() + './Rooms/hall.png').scaled(sizeimport[3], sizeimport[3])
    hall.setPixmap(hallImg)

    # These are all the halls between column 2 & 3
    hallway8 = QLabel(self)
    hallway8.setGeometry(7*sizeimport[2], sizeimport[2], sizeimport[2], sizeimport[2])
    hallway8.setPixmap(hallwayImg_v)

    hallway9 = QLabel(self)
    hallway9.setGeometry(7*sizeimport[2], 5*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway9.setPixmap(hallwayImg_v)

    hallway10 = QLabel(self)
    hallway10.setGeometry(7*sizeimport[2], 9*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway10.setPixmap(hallwayImg_v)

    # These are all the rooms in column 3
    lounge = QLabel(self)
    lounge.setGeometry(8*sizeimport[2], 0, sizeimport[3], sizeimport[3])
    loungeImg = QPixmap(os.getcwd() + './Rooms/lounge.png').scaled(sizeimport[3], sizeimport[3])
    lounge.setPixmap(loungeImg)

    hallway11 = QLabel(self)
    hallway11.setGeometry(9*sizeimport[2], 3*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway11.setPixmap(hallwayImg)

    dining = QLabel(self)
    dining.setGeometry(8*sizeimport[2], 4*sizeimport[2], sizeimport[3], sizeimport[3])
    diningImg = QPixmap(os.getcwd() + './Rooms/dining_room.png').scaled(sizeimport[3], sizeimport[3])
    dining.setPixmap(diningImg)

    hallway12 = QLabel(self)
    hallway12.setGeometry(9*sizeimport[2], 7*sizeimport[2], sizeimport[2], sizeimport[2])
    hallway12.setPixmap(hallwayImg)

    kitchen = QLabel(self)
    kitchen.setGeometry(8*sizeimport[2], 8*sizeimport[2], sizeimport[3], sizeimport[3])
    kitchenImg = QPixmap(os.getcwd() + './Rooms/kitchen.png').scaled(sizeimport[3], sizeimport[3])
    kitchen.setPixmap(kitchenImg)


  def player_setup(self, name, j, i):
    sizeimport = self.sizes()
    p = [(0*sizeimport[2]+sizeimport[5]), (1*sizeimport[2]+sizeimport[5]), (2*sizeimport[2]+sizeimport[5]), (3*sizeimport[2]+sizeimport[5]), (4*sizeimport[2]+sizeimport[5]), (5*sizeimport[2]+sizeimport[5]), (6*sizeimport[2]+sizeimport[5]), (7*sizeimport[2]+sizeimport[5]), (8*sizeimport[2]+sizeimport[5]), (9*sizeimport[2]+sizeimport[5]), (10*sizeimport[2]+sizeimport[5])]

    if name == "Miss Scarlet":
      scarlet = QLabel(self)
      redIcon = QPixmap(os.getcwd() + './Players/red.png').scaledToHeight(sizeimport[4])
      scarlet.move(p[i], p[j])
      scarlet.setPixmap(redIcon)
      scarlet.show()
    if name == "Colonel Mustard":
      mustard = QLabel(self)
      brownIcon = QPixmap(os.getcwd() + './Players/brown.png').scaledToHeight(sizeimport[4])
      mustard.move(p[i], p[j])
      mustard.setPixmap(brownIcon)
      mustard.show()
    if name == "Mrs. White":
      white = QLabel(self)
      greyIcon = QPixmap(os.getcwd() + './Players/grey.png').scaledToHeight(sizeimport[4])
      white.move(p[i], p[j])
      white.setPixmap(greyIcon)
      white.show()
    if name == "Mr. Green":
      green = QLabel(self)
      greenIcon = QPixmap(os.getcwd() + './Players/green.png').scaledToHeight(sizeimport[4])
      green.move(p[i], p[j])
      green.setPixmap(greenIcon)
      green.show()
    if name == "Mrs. Peacock":
      peacock = QLabel(self)
      blueIcon = QPixmap(os.getcwd() + './Players/blue.ico').scaledToHeight(sizeimport[4])
      peacock.move(p[i], p[j])
      peacock.setPixmap(blueIcon)
      peacock.show()
    if name == "Professor Plum":
      plum = QLabel(self)
      purpleIcon = QPixmap(os.getcwd() + './Players/purple.png').scaledToHeight(sizeimport[4])
      plum.move(p[i], p[j])
      plum.setPixmap(purpleIcon)
      plum.show()

  def weapon_setup(self, name, j, i):
    sizeimport = self.sizes()
    p = [(0*sizeimport[2]), (1*sizeimport[2]), (2*sizeimport[2]), (3*sizeimport[2]), (4*sizeimport[2]), (5*sizeimport[2]), (6*sizeimport[2]), (7*sizeimport[2]), (8*sizeimport[2]), (9*sizeimport[2]), (10*sizeimport[2])]

    if name == "Wrench":
      wrench = QLabel(self)
      wrenchIcon = QPixmap(os.getcwd() + './Weapons/wrench.ico').scaledToHeight(sizeimport[4])
      wrench.move(p[i], p[j])
      wrench.setPixmap(wrenchIcon)
      wrench.show()

    if name == "Rope":
      rope = QLabel(self)
      ropeIcon = QPixmap(os.getcwd() + './Weapons/Rope.ico').scaledToHeight(sizeimport[4])
      rope.move(p[i], p[j])
      rope.setPixmap(ropeIcon)
      rope.show()
    if name == "Revolver":
      revolver = QLabel(self)
      revolverIcon = QPixmap(os.getcwd() + './Weapons/revolver.ico').scaledToHeight(sizeimport[4])
      revolver.move(p[i], p[j])
      revolver.setPixmap(revolverIcon)
      revolver.show()

    if name == "knife":
      knife = QLabel(self)
      knifeIcon = QPixmap(os.getcwd() + './Weapons/knife.ico').scaledToHeight(sizeimport[4])
      knife.move(p[i], p[j])
      knife.setPixmap(knifeIcon)
      knife.show()

    if name == "Candlestick":
      candlestick = QLabel(self)
      candlestickIcon = QPixmap(os.getcwd() + './Weapons/candlestick.ico').scaledToHeight(sizeimport[4])
      candlestick.move(p[i], p[j])
      candlestick.setPixmap(candlestickIcon)
      candlestick.show()

    if name == "Lead Pipe":
      pipe = QLabel(self)
      pipeIcon = QPixmap(os.getcwd() + './Weapons/pipe.ico').scaledToHeight(sizeimport[4])
      pipe.move(p[i], p[j])
      pipe.setPixmap(pipeIcon)
      pipe.show()

  def detective_notes(self):
    sizeimport = self.sizes()
    notes = QWidget(self)
    suspects = QWidget(self)
    weapons = QWidget(self)
    rooms = QWidget(self)
    notes.setGeometry((sizeimport[1]), 0, (sizeimport[0]-sizeimport[1]), sizeimport[1])

    Title1 = QLabel(self)
    Title1.setStyleSheet(" font-size: 30px; font-style: bold; qproperty-alignment: AlignCenter; font-family: Times New Roman;")
    Title2 = QLabel(self)
    Title2.setStyleSheet(" font-size: 20px; font-style: bold; qproperty-alignment: AlignLeft; font-family: Times New Roman;")
    Title3 = QLabel(self)
    Title3.setStyleSheet(" font-size: 20px; font-style: bold; qproperty-alignment: AlignLeft; font-family: Times New Roman;")
    Title4 = QLabel(self)
    Title4.setStyleSheet(" font-size: 20px; font-style: bold; qproperty-alignment: AlignLeft; font-family: Times New Roman;")

    Suspect1 = QLabel(self)
    Suspect2 = QLabel(self)
    Suspect3 = QLabel(self)
    Suspect4 = QLabel(self)
    Suspect5 = QLabel(self)
    Suspect6 = QLabel(self)

    Weapon1 = QLabel(self)
    Weapon2 = QLabel(self)
    Weapon3 = QLabel(self)
    Weapon4 = QLabel(self)
    Weapon5 = QLabel(self)
    Weapon6 = QLabel(self)

    Room1 = QLabel(self)
    Room2 = QLabel(self)
    Room3 = QLabel(self)
    Room4 = QLabel(self)
    Room5 = QLabel(self)
    Room6 = QLabel(self)
    Room7 = QLabel(self)
    Room8 = QLabel(self)
    Room9 = QLabel(self)

    TextEdit = QTextEdit(self)

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


    suspect_grid = QGridLayout()
    suspect_grid.addWidget(Suspect1, 0, 0)
    suspect_grid.addWidget(Suspect2, 1, 0)
    suspect_grid.addWidget(Suspect3, 2, 0)
    suspect_grid.addWidget(Suspect4, 0, 1)
    suspect_grid.addWidget(Suspect5, 1, 1)
    suspect_grid.addWidget(Suspect6, 2, 1)

    suspects.setLayout(suspect_grid)

    weapon_grid = QGridLayout()
    weapon_grid.addWidget(Weapon1, 0, 0)
    weapon_grid.addWidget(Weapon2, 1, 0)
    weapon_grid.addWidget(Weapon3, 2, 0)
    weapon_grid.addWidget(Weapon4, 0, 1)
    weapon_grid.addWidget(Weapon5, 1, 1)
    weapon_grid.addWidget(Weapon6, 2, 1)

    weapons.setLayout(weapon_grid)

    room_grid = QGridLayout()
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

    vbox = QVBoxLayout()
    vbox.addWidget(Title1)
    vbox.addWidget(Title2)
    vbox.addWidget(suspects)
    vbox.addWidget(Title3)
    vbox.addWidget(rooms)
    vbox.addWidget(Title4)
    vbox.addWidget(weapons)
    vbox.addWidget(TextEdit)

    notes.setLayout(vbox)


if __name__ == '__main__':
  app = QApplication(sys.argv)
  gameBoardGUI = BoardGUI()
  gameBoardGUI.init_ui()
  app.exec_()
