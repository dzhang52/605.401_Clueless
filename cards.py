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
        roomCard = random.choice(self.roomCards)
        weaponCard = random.choice(self.weaponCards)
        characterCard = random.choice(self.characterCards)

        self.roomCards.remove(roomCard)
        self.weaponCards.remove(weaponCard)
        self.characterCards.remove(characterCard)

        secretEnvelope = [roomCard, weaponCard, characterCard]
        return secretEnvelope
    
    def dealCards(self, players):
        allCards = self.roomCards + self.weaponCards + self.characterCards
        remainingCards = len(allCards)
        playerCounter = 0

        while remainingCards > 0:
            randomCard = random.choice(allCards)
            players[playerCounter].cards.append(randomCard)
            allCards.remove(randomCard)

            playerCounter = (playerCounter + 1) % len(players)
            remainingCards -= 1

        self.roomCards = []
        self.weaponCards = []
        self.characterCards = []
            

if __name__ == '__main__':
    cardDeck = CardDeck()
    print cardDeck.roomCards

    print cardDeck.dealSecretEnvelope()
    

