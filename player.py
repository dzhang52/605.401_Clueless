class Player(object):
    
    def __init__(self, conn, addr, name):
        self.conn = conn
        self.addr = addr
        self.name = name
        self.character = None
        self.cards = []
        self.madeAccusation = False
        self.madeSuggestion = False
        self.madeMovement = False

    def refresh(self):
        self.madeMovement = False
        self.madeSuggestion = False