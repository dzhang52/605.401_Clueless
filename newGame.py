import socket, select, string, sys, os, errno

from PySide.QtCore import *
from PySide.QtGui import *

class EnterNameWindow(QWidget):
  def __init__(self, socketS):
    super(EnterNameWindow, self).__init__()
    self.setFixedSize(400, 200)
    self.socketS = socketS
    

    self.nameLabel = QLabel()
    self.nameLabel.setText("Please Enter Your Name")
    self.name = QLineEdit()
    #self.name_assignment()

    self.okay = QPushButton("Okay")
    self.okay.clicked.connect(self.set_name)
    self.cancel = QPushButton("Cancel")
    self.cancel.clicked.connect(exit)

    hbox1 = QWidget()
    hbox1layout = QHBoxLayout()
    hbox1layout.addWidget(self.nameLabel)
    hbox1layout.addWidget(self.name)
    hbox1.setLayout(hbox1layout)

    hbox4 = QWidget()
    hbox4layout = QHBoxLayout()
    hbox4layout.stretch(1)
    hbox4layout.addWidget(self.okay)
    hbox4layout.addWidget(self.cancel)
    hbox4.setLayout(hbox4layout)

    layout = QVBoxLayout()
    layout.addWidget(hbox1)
    #layout.addWidget(hbox2)
    #layout.addWidget(hbox3)
    layout.addStretch(1)
    layout.addWidget(hbox4)

    self.setLayout(layout)
    self.setWindowTitle("Enter your name")

  def set_name(self):
    self.socketS.send(self.name.text())
    self.close()

  def name_assignment(self):
    return self.name.text()

class StartupWindow(QWidget):
  def __init__(self, socketS):
    super(StartupWindow, self).__init__()
    self.socketS = socketS
    #self.globalMessage = "Start of the globalMessage"

    self.setFixedSize(600, 500)
    #self.nameLabel = QLabel()
    #self.nameLabel.setText("Please Enter Your Name")
    # self.name = QLineEdit()
    # self.name_assignment()
    self.res = QLabel()
    self.res.setText("Please set your Resolution")
    self.cb = QComboBox()
    self.cb.addItems(["1150x715", "1325x825", "1750x1100", "2010x1375", "2650x1650"])
    self.cb.currentIndexChanged.connect(self.res_assignment)
    #self.playerpick = QLabel()
    #self.playerpick.setText("Please choose your Player")
    #self.cbplayer = QComboBox()
    #self.cbplayer.addItems(["Colonel Mustard", "Miss Scarlet", "Professor Plum", "Mr. Green", "Mrpys. White", "Mrs. Peacock"])
    #self.cbplayer.currentIndexChanged.connect(self.player_assignment)

    self.accept = QPushButton("Start Game")
    self.accept.clicked.connect(self.start_game)
    self.cancel = QPushButton("Cancel")
    self.cancel.clicked.connect(exit)

    # hbox1 = QWidget()
    # hbox1layout = QHBoxLayout()
    # hbox1layout.addWidget(self.nameLabel)
    # hbox1layout.addWidget(self.name)
    # hbox1.setLayout(hbox1layout)

    # hbox2 = QWidget()
    # hbox2layout = QHBoxLayout()
    # hbox2layout.stretch(1)
    # hbox2layout.addWidget(self.playerpick)
    # hbox2layout.addWidget(self.cbplayer)
    # hbox2.setLayout(hbox2layout)

    hbox3 = QWidget()
    hbox3layout = QHBoxLayout()
    hbox3layout.stretch(1)
    hbox3layout.addWidget(self.res)
    hbox3layout.addWidget(self.cb)
    hbox3.setLayout(hbox3layout)

    hbox4 = QWidget()
    hbox4layout = QHBoxLayout()
    hbox4layout.stretch(1)
    hbox4layout.addWidget(self.accept)
    hbox4layout.addWidget(self.cancel)
    hbox4.setLayout(hbox4layout)

    layout = QVBoxLayout()
    # layout.addWidget(hbox1)
    # layout.addWidget(hbox2)
    layout.addWidget(hbox3)
    layout.addStretch(1)
    layout.addWidget(hbox4)

    self.setLayout(layout)
    self.setWindowTitle("combo box demo")

    # timer = QTimer(self)
    # timer.timeout.connect(self.check_if_game_started)
    # timer.start(3000)

  def player_assignment(self):
    return self.cbplayer.currentText()

  def res_assignment(self):
    return [int(self.cb.currentText().split("x")[0]), int(self.cb.currentText().split("x")[1])]

  def start_game(self):
    self.socketS.send("Start Game\n")
    self.close()

  def updateGlobalMessage(self, globalMessage):
    self.globalMessage = globalMessage
    
  def printGlobalMessage(self):
    print self.globalMessage

  def updateFromServer(self):
    print("closing StartupWindow because someone started the game")
    self.close()

  def check_if_game_started(self):
    global globalResponse
    print globalResponse

class EnterCharWindow(QWidget):
  def __init__(self, socketS, charList):
    super(EnterCharWindow, self).__init__()
    self.setFixedSize(400, 200)
    self.socketS = socketS
    

    self.playerpick = QLabel()
    self.playerpick.setText("Please choose your character")
    self.cbplayer = QComboBox()
    self.cbplayer.addItems(charList)
    #self.cbplayer.currentIndexChanged.connect(self.player_assignment)

    self.okay = QPushButton("Okay")
    self.okay.clicked.connect(self.set_char)
    self.cancel = QPushButton("Cancel")
    self.cancel.clicked.connect(exit)

    hbox2 = QWidget()
    hbox2layout = QHBoxLayout()
    hbox2layout.stretch(1)
    hbox2layout.addWidget(self.playerpick)
    hbox2layout.addWidget(self.cbplayer)
    hbox2.setLayout(hbox2layout)

    hbox4 = QWidget()
    hbox4layout = QHBoxLayout()
    hbox4layout.stretch(1)
    hbox4layout.addWidget(self.okay)
    hbox4layout.addWidget(self.cancel)
    hbox4.setLayout(hbox4layout)

    layout = QVBoxLayout()
    #layout.addWidget(hbox1)
    layout.addWidget(hbox2)
    #layout.addWidget(hbox3)
    layout.addStretch(1)
    layout.addWidget(hbox4)

    self.setLayout(layout)
    self.setWindowTitle("Pick a character")

  def set_char(self):
    self.socketS.send(str(self.cbplayer.currentIndex()))
    self.close()

  def name_assignment(self):
    return self.name.text()

#if __name__ == '__main__':
#  app = QApplication(sys.argv)
#  ex = startup()
#  ex.show()
#  app.exec_()
#  print(ex.name_assignment())
#  print(ex.player_assignment())
#  print(ex.res_assignment())
