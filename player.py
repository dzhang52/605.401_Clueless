class Player(object):
  def __init__(self, conn, addr, name):
    self.conn = conn
    self.addr = addr
    self.name = name
    self.character = ""
    self.cards = []