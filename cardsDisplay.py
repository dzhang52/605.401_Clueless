import os, sys

from PySide.QtGui import *
class cardsGUI(QWidget):

  def __init__(self):
    super(cardsGUI, self).__init__()
    self.cardslist = ['Colonel Mustard', 'Miss Scarlet', 'Mr. Green', 'Professor Plum', 'Mrs. Peacock', 'Mrs. White', \
                      'Candlestick', 'Wrench', 'Rope', 'Revolver', 'Knife', 'Lead Pipe', \
                      'Billiard Room', 'Conservatory', 'Study', 'Ballroom', 'Dining Room', 'Kitchen', 'Lounge', 'Hall', 'Library']


  def init_ui(self):
    self.setWindowTitle("Clueless")
    self.setWindowIcon(QIcon('mag.png'))
    hbox = QHBoxLayout(self)
    self.displayCards(hbox)
    self.show()

  def displayCards(self, layout):
    for name in self.cardslist:
      imagename = self.cardTranslation(name)
      imagemap = QPixmap('Cards\\' + imagename)
      lbl = QLabel(self)
      lbl.setPixmap(imagemap)
      layout.addWidget(lbl)

  def cardTranslation(self, input):
    return {
      'Colonel Mustard': 'mustard_card.PNG',
      'Miss Scarlet': 'scarlet_card.PNG',
      'Mr. Green': 'green_card.PNG',
      'Professor Plum': 'plum_card.PNG',
      'Mrs. Peacock': 'peacock_card.PNG',
      'Mrs. White': 'white_card.PNG',
      'Candlestick': 'candlestick_card.PNG',
      'Wrench': 'wrench_card.PNG',
      'Rope': 'rope_card.PNG',
      'Revolver': 'revolver_card.PNG',
      'Knife': 'knife_card.PNG',
      'Lead Pipe': 'pipe_card.PNG',
      'Billiard Room': 'billiards_card.PNG',
      'Conservatory': 'conservatory_card.PNG',
      'Study': 'study_card.PNG',
      'Ballroom': 'ball_card.PNG',
      'Dining Room': 'dining_card.PNG',
      'Kitchen': 'kitchen_card.PNG',
      'Lounge': 'lounge_card.PNG',
      'Hall': 'hall_card.PNG',
      'Library': 'library_card.PNG'
    }[input]


if __name__ == '__main__':
  app = QApplication(sys.argv)
  cardsGUI = cardsGUI()
  cardsGUI.init_ui()
  app.exec_()

