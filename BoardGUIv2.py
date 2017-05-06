import os, sys, math

from PySide.QtCore import Qt
from PySide import QtCore
from PySide.QtGui import *
from PySide.QtCore import QPoint

global i
global j

class BoardGUI(QWidget):

  def __init__(self):
    global i
    global j
    super(BoardGUI, self).__init__()
    self.i = 2010
    self.j = 1375
    i = self.i
    j = self.j
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


  def boardlayout(self):
    roomsize = self.sizes()[1]
    rooms = QWidget()
    rooms.setFixedSize(roomsize, roomsize)
    grid = QGridLayout()
    grid.setSpacing(0)
    ball = QPixmap('Rooms\\ballroom.PNG')
    bill = QPixmap('Rooms\\billiards_room.PNG')
    cons = QPixmap('Rooms\\conservatory.PNG')
    dini = QPixmap('Rooms\\dining_room.PNG')
    hall = QPixmap('Rooms\\hall.PNG')
    h_hz = QPixmap('Rooms\\hallway_horizontal.PNG')
    h_vt = QPixmap('Rooms\\hallway_vertical.PNG')
    kitc = QPixmap('Rooms\\kitchen.PNG')
    libr = QPixmap('Rooms\\library.PNG')
    loun = QPixmap('Rooms\\lounge.PNG')
    stud = QPixmap('Rooms\\study.PNG')




    lbl1 = QLabelplus(self)
    lbl1.setPixmap(stud)
    lbl2 = QLabelplus(self)
    lbl2.setPixmap(ball)
    lbl3 = QLabelplus(self)
    lbl3.setPixmap(loun)
    lbl4 = QLabelplus(self)
    lbl4.setPixmap(libr)
    lbl5 = QLabelplus(self)
    lbl5.setPixmap(bill)
    lbl6 = QLabelplus(self)
    lbl6.setPixmap(dini)
    lbl7 = QLabelplus(self)
    lbl7.setPixmap(cons)
    lbl8 = QLabelplus(self)
    lbl8.setPixmap(hall)
    lbl9 = QLabelplus(self)
    lbl9.setPixmap(kitc)

    lbl10 = QLabelplus(self)
    lbl10.setPixmap(h_hz)
    lbl11 = QLabelplus(self)
    lbl11.setPixmap(h_hz)
    lbl12 = QLabelplus(self)
    lbl12.setPixmap(h_hz)
    lbl13 = QLabelplus(self)
    lbl13.setPixmap(h_hz)
    lbl14 = QLabelplus(self)
    lbl14.setPixmap(h_hz)
    lbl15 = QLabelplus(self)
    lbl15.setPixmap(h_hz)

    lbl16 = QLabelplus(self)
    lbl16.setPixmap(h_vt)
    lbl17 = QLabelplus(self)
    lbl17.setPixmap(h_vt)
    lbl18 = QLabelplus(self)
    lbl18.setPixmap(h_vt)
    lbl19 = QLabelplus(self)
    lbl19.setPixmap(h_vt)
    lbl20 = QLabelplus(self)
    lbl20.setPixmap(h_vt)
    lbl21 = QLabelplus(self)
    lbl21.setPixmap(h_vt)


    lbllist = [lbl1, lbl2, lbl3, lbl4, lbl5, lbl6, lbl7, lbl8, lbl9, lbl10, lbl11, lbl12, lbl13, lbl14, lbl15, lbl16, \
               lbl17, lbl18, lbl19, lbl20,  lbl21]
    for lbl in lbllist:
      lbl.setScaledContents(True)
      lbl.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

    grid.addWidget(lbl1, 0, 0, 3, 3)
    grid.addWidget(lbl2, 0, 5, 3, 3)
    grid.addWidget(lbl3, 0, 9, 3, 3)
    grid.addWidget(lbl4, 5, 0, 3, 3)
    grid.addWidget(lbl5, 5, 5, 3, 3)
    grid.addWidget(lbl6, 5, 9, 3, 3)
    grid.addWidget(lbl7, 9, 0, 3, 3)
    grid.addWidget(lbl8, 9, 5, 3, 3)
    grid.addWidget(lbl9, 9, 9, 3, 3)

    grid.addWidget(lbl10, 1, 4, 1, 1)
    grid.addWidget(lbl11, 1, 8, 1, 1)
    grid.addWidget(lbl12, 6, 4, 1, 1)
    grid.addWidget(lbl13, 6, 8, 1, 1)
    grid.addWidget(lbl14, 10, 4, 1, 1)
    grid.addWidget(lbl15, 10, 8, 1, 1)

    grid.addWidget(lbl16, 4, 1, 1, 1)
    grid.addWidget(lbl17, 4, 6, 1, 1)
    grid.addWidget(lbl18, 4, 10, 1, 1)
    grid.addWidget(lbl19, 8, 1, 1, 1)
    grid.addWidget(lbl20, 8, 6, 1, 1)
    grid.addWidget(lbl21, 8, 10, 1, 1)
    rooms.setLayout(grid)
    print(self.size().height())
    self.roomlayout = QGridLayout()
    self.roomlayout.setAlignment(QtCore.Qt.AlignLeft)
    self.roomlayout.addWidget(rooms)
    self.setLayout(self.roomlayout)



  def player_setup(self, name, j, i):
    sizeimport = self.sizes()
    p = [(0*sizeimport[2]+sizeimport[5]), (1*sizeimport[2]+sizeimport[5]), (2*sizeimport[2]+sizeimport[5]), (3*sizeimport[2]+sizeimport[5]), (4*sizeimport[2]+sizeimport[5]), (5*sizeimport[2]+sizeimport[5]), (6*sizeimport[2]+sizeimport[5]), (7*sizeimport[2]+sizeimport[5]), (8*sizeimport[2]+sizeimport[5]), (9*sizeimport[2]+sizeimport[5]), (10*sizeimport[2]+sizeimport[5])]

    if name == "Miss Scarlet":
      scarlet = QLabel(self)
      redIcon = QPixmap(os.getcwd() + './Players/red.png').scaledToHeight(sizeimport[4])
      scarlet.move(p[i], p[j])
      scarlet.setPixmap(redIcon)
    if name == "Colonel Mustard":
      mustard = QLabel(self)
      brownIcon = QPixmap(os.getcwd() + './Players/brown.png').scaledToHeight(sizeimport[4])
      mustard.move(p[i], p[j])
      mustard.setPixmap(brownIcon)
    if name == "Mrs. White":
      white = QLabel(self)
      greyIcon = QPixmap(os.getcwd() + './Players/grey.png').scaledToHeight(sizeimport[4])
      white.move(p[i], p[j])
      white.setPixmap(greyIcon)
    if name == "Mr. Green":
      green = QLabel(self)
      greenIcon = QPixmap(os.getcwd() + './Players/green.png').scaledToHeight(sizeimport[4])
      green.move(p[i], p[j])
      green.setPixmap(greenIcon)
    if name == "Mrs. Peacock":
      peacock = QLabel(self)
      blueIcon = QPixmap(os.getcwd() + './Players/blue.ico').scaledToHeight(sizeimport[4])
      peacock.move(p[i], p[j])
      peacock.setPixmap(blueIcon)
    if name == "Professor Plum":
      plum = QLabel(self)
      purpleIcon = QPixmap(os.getcwd() + './Players/purple.png').scaledToHeight(sizeimport[4])
      plum.move(p[i], p[j])
      plum.setPixmap(purpleIcon)

  def weapon_setup(self, name, j, i):
    sizeimport = self.sizes()
    p = [(0*sizeimport[2]), (1*sizeimport[2]), (2*sizeimport[2]), (3*sizeimport[2]), (4*sizeimport[2]), (5*sizeimport[2]), (6*sizeimport[2]), (7*sizeimport[2]), (8*sizeimport[2]), (9*sizeimport[2]), (10*sizeimport[2])]

    if name == "Wrench":
      scarlet = QLabel(self)
      redIcon = QPixmap(os.getcwd() + './Weapons/wrench.ico').scaledToHeight(sizeimport[4])
      scarlet.move(p[i], p[j])
      scarlet.setPixmap(redIcon)
    if name == "Rope":
      mustard = QLabel(self)
      brownIcon = QPixmap(os.getcwd() + './Weapons/Rope.ico').scaledToHeight(sizeimport[4])
      mustard.move(p[i], p[j])
      mustard.setPixmap(brownIcon)
    if name == "Revolver":
      white = QLabel(self)
      greyIcon = QPixmap(os.getcwd() + './Weapons/revolver.ico').scaledToHeight(sizeimport[4])
      white.move(p[i], p[j])
      white.setPixmap(greyIcon)
    if name == "knife":
      green = QLabel(self)
      greenIcon = QPixmap(os.getcwd() + './Weapons/knife.ico').scaledToHeight(sizeimport[4])
      green.move(p[i], p[j])
      green.setPixmap(greenIcon)
    if name == "Candlestick":
      peacock = QLabel(self)
      blueIcon = QPixmap(os.getcwd() + './Weapons/candlestick.ico').scaledToHeight(sizeimport[4])
      peacock.move(p[i], p[j])
      peacock.setPixmap(blueIcon)
    if name == "Lead Pipe":
      plum = QLabel(self)
      purpleIcon = QPixmap(os.getcwd() + './Weapons/pipe.ico').scaledToHeight(sizeimport[4])
      plum.move(p[i], p[j])
      plum.setPixmap(purpleIcon)

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

class QLabelplus(QLabel):
  def __init__(self, parent=None):
    super(QLabelplus, self).__init__(parent)
    self.setMouseTracking(True)


  def enterEvent(self, event):
    self.setStyleSheet("border:10px solid rgb(0, 255, 0);")

  def leaveEvent(self, event):
    self.setStyleSheet("border:0px")

  def mousePressEvent(self, event):
    global j
    position2 = QPoint(self.pos().x(), self.pos().y())
    unit = (((j-36)/11))
    x = (self.pos().x()-18)/(unit)
    y = (self.pos().y()-18)/(unit)
    print(str(x) + ", " + str(y))
    print(int(unit))

if __name__ == '__main__':
  app = QApplication(sys.argv)
  gameBoardGUI = BoardGUI()
  gameBoardGUI.init_ui()
  app.exec_()
