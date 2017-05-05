class Player(object):
  def __init__(self, conn, addr, name, character):
    self.conn = conn
    self.addr = addr
    self.name = name
    self.character = character
    self.cards = []