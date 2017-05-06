import sys
from PySide.QtCore import *
from PySide.QtGui import *

class startup(QWidget):
  def __init__(self, parent=None):
    super(startup, self).__init__(parent)
    self.setFixedSize(600, 500)
    self.nameLabel = QLabel()
    self.nameLabel.setText("Please Enter Your Name")
    self.name = QLineEdit()
    self.name_assignment()
    self.res = QLabel()
    self.res.setText("Please set your Resolution")
    self.cb = QComboBox()
    self.cb.addItems(["1150x715", "1325x825", "1750x1100", "2010x1375", "2650x1650"])
    self.cb.currentIndexChanged.connect(self.res_assignment)
    self.playerpick = QLabel()
    self.playerpick.setText("Please choose your Player")
    self.cbplayer = QComboBox()
    self.cbplayer.addItems(["Colonel Mustard", "Miss Scarlet", "Professor Plum", "Mr. Green", "Mrs. White", "Mrs. Peacock"])
    self.cbplayer.currentIndexChanged.connect(self.player_assignment)
    self.accept = QPushButton("Start Game")
    self.accept.clicked.connect(self.close)
    self.cancel = QPushButton("Cancel")
    self.cancel.clicked.connect(exit)

    hbox1 = QWidget()
    hbox1layout = QHBoxLayout()
    hbox1layout.addWidget(self.nameLabel)
    hbox1layout.addWidget(self.name)
    hbox1.setLayout(hbox1layout)

    hbox2 = QWidget()
    hbox2layout = QHBoxLayout()
    hbox2layout.stretch(1)
    hbox2layout.addWidget(self.playerpick)
    hbox2layout.addWidget(self.cbplayer)
    hbox2.setLayout(hbox2layout)

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
    layout.addWidget(hbox1)
    layout.addWidget(hbox2)
    layout.addWidget(hbox3)
    layout.addStretch(1)
    layout.addWidget(hbox4)

    self.setLayout(layout)
    self.setWindowTitle("combo box demo")

  def name_assignment(self):
    return self.name.text()

  def player_assignment(self):
    return str(self.cbplayer.currentIndex())

  def res_assignment(self):
    return [int(self.cb.currentText().split("x")[0]), int(self.cb.currentText().split("x")[1])]

#if __name__ == '__main__':
#  app = QApplication(sys.argv)
#  ex = startup()
#  ex.show()
#  app.exec_()
#  print(ex.name_assignment())
#  print(ex.player_assignment())
#  print(ex.res_assignment())
