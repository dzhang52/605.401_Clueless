import sys
from PySide.QtCore import *
from PySide.QtGui import *

class startup(QWidget):
  def __init__(self, parent=None):
    super(startup, self).__init__(parent)
    self.setFixedSize(2000, 2000)
    self.setWindowTitle("Clueless")
    self.setWindowIcon(QIcon('mag.png'))



    testwidget = QWidget()
    grid = QGridLayout()
    grid.setSpacing(0)
    imagemap1 = QPixmap('Cards\\ball_card.PNG')
    imagemap2 = QPixmap('Cards\\billiards_card.PNG')
    imagemap3 = QPixmap('Cards\\clue_card.PNG')
    imagemap4 = QPixmap('Cards\\green_card.PNG')
    imagemap5 = QPixmap('Cards\\plum_card.PNG')
    imagemap6 = QPixmap('Cards\\study_card.PNG')
    lbl1 = QLabelplus(self)
    lbl1.setPixmap(imagemap1)
    lbl1.setScaledContents(True)
    lbl1.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
    lbl1.setStyleSheet("border:1px solid rgb(0, 255, 0);")
    lbl2 = QLabelplus(self)
    lbl2.setPixmap(imagemap2)
    lbl2.setScaledContents(True)
    lbl2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
    lbl2.setStyleSheet("border:1px solid rgb(0, 255, 0);")
    lbl3 = QLabelplus(self)
    lbl3.setPixmap(imagemap3)
    lbl3.setScaledContents(True)
    lbl3.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
    lbl3.setStyleSheet("border:1px solid rgb(0, 255, 0);")
    lbl4 = QLabelplus(self)
    lbl4.setPixmap(imagemap4)
    lbl4.setScaledContents(True)
    lbl4.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
    lbl4.setStyleSheet("border:1px solid rgb(0, 255, 0);")
    lbl5 = QLabelplus(self)
    lbl5.setPixmap(imagemap5)
    lbl5.setScaledContents(True)
    lbl5.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
    lbl5.setStyleSheet("border:1px solid rgb(0, 255, 0);")
    lbl6 = QLabelplus(self)
    lbl6.setPixmap(imagemap6)
    lbl6.setScaledContents(True)
    lbl6.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
    lbl6.setStyleSheet("border:1px solid rgb(0, 255, 0);")
    grid.addWidget(lbl1,0,0,3,3)
    grid.addWidget(lbl2,1,4,1,1)
    grid.addWidget(lbl3,0,5,3,3)
    grid.addWidget(lbl4,1,8,1,1)
    grid.addWidget(lbl5,0,9,3,3)
    grid.addWidget(lbl6,4,1,1,1)
    testwidget.setLayout(grid)

    self.testlayout = QGridLayout()
    self.testlayout.addWidget(testwidget)
    self.testlayout.addWidget(QLabel("test"))
    self.setLayout(self.testlayout)

class QLabelplus(QLabel):
    def __init__(self, parent=None):
      super(QLabelplus, self).__init__(parent)
      self.setMouseTracking(True)

    def enterEvent(self, event):
      print("Enter")
      self.setStyleSheet("border:10px solid rgb(0, 255, 0);")

    def leaveEvent(self, event):
      self.setStyleSheet("border:0px")
      print("Leave")


    '''
    label1 = QLabel('label 1')
    line_edit1 = QLineEdit()
    sublayout1 = QVBoxLayout()
    sublayout1.addWidget(label1)
    sublayout1.addWidget(line_edit1)

    label2 = QLabel('label 2')
    line_edit2 = QLineEdit()
    sublayout2 = QVBoxLayout()
    sublayout2.addWidget(label2)
    sublayout2.addWidget(line_edit2)

    button1 = QPushButton("button1")
    button2 = QPushButton("button2")
    button3 = QPushButton("button3")

    grid_layout = QGridLayout(self)
    grid_layout.addLayout(sublayout1, 0, 0, 1, 2)
    grid_layout.addLayout(sublayout2, 1, 0, 1, 2)
    grid_layout.addWidget(button1, 2, 0, 1, 1)
    grid_layout.addWidget(button2, 2, 1, 1, 1)
    grid_layout.addWidget(button3, 2, 2, 1, 1)

    
    
    

    imagemap1 = QPixmap('Cards\\ball_card.PNG').scaled(150, 150)
    imagemap2 = QPixmap('Cards\\ball_card.PNG').scaled(150, 150)
    imagemap3 = QPixmap('Cards\\ball_card.PNG').scaled(150, 150)
    imagemap4 = QPixmap('Cards\\ball_card.PNG').scaled(150, 150)
    imagemap5 = QPixmap('Cards\\ball_card.PNG').scaled(150, 150)
    imagemap6 = QPixmap('Cards\\hall_card.PNG').scaled(150, 150)
    lbl1 = QLabel(self)
    lbl1.setPixmap(imagemap1)
    lbl2 = QLabel(self)
    lbl2.setPixmap(imagemap2)
    lbl3 = QLabel(self)
    lbl3.setPixmap(imagemap3)
    lbl4 = QLabel(self)
    lbl4.setPixmap(imagemap4)
    lbl5 = QLabel(self)
    lbl5.setPixmap(imagemap5)
    lbl6 = QLabel(self)
    lbl6.setPixmap(imagemap6)
    grid.addWidget(lbl1,0,0)
    grid.addWidget(lbl2,0,1)
    grid.addWidget(lbl3,0,2)
    grid.addWidget(lbl4,1,0)
    grid.addWidget(lbl5,1,1)
    grid.addWidget(lbl6,1,2)
    '''
    #
'''
    def window():
      app = QApplication(sys.argv)
      win = QWidget()
      grid = QGridLayout()

      for i in range(1, 5):
        for j in range(1, 5):
          grid.addWidget(QPushButton("B" + str(i) + str(j)), i, j)

      win.setLayout(grid)
      win.setGeometry(100, 100, 200, 100)
      win.setWindowTitle("PyQt")
      win.show()
      sys.exit(app.exec_())

  if __name__ == '__main__':
    window()
'''


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = startup()
  ex.show()
  app.exec_()
