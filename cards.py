import random

class CardDeck(object):
    roomCards = ["Study", 
                 "Hall", 
                 "Lounge", 
                 "Library", 
                 "Billiard Room", 
                 "Dining Room", 
                 "Conservatory", 
                 "Ballroom" ,
                 "Kitchen"]

    weaponCards = ["Rope", 
                   "Lead Pipe",
                   "Knife",
                   "Wrench",
                   "Candlestick",
                   "Revolver"]
    
    characterCards = ["Colonel Mustard",
                      "Miss Scarlet",
                      "Professor Plum",
                      "Mr. Green",
                      "Mrs. White",
                      "Mrs. Peacock"]

    
    def dealSecretEnvelope(self):
        secretEnvelope = [random.choice(self.roomCards),random.choice(self.weaponCards), random.choice(self.characterCards)]
        return secretEnvelope

if __name__ == '__main__':
    cardDeck = CardDeck()
    print cardDeck.roomCards

    print cardDeck.dealSecretEnvelope()
    

