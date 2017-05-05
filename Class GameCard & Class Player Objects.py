class GameCard(object):
    """
    represents a single Clue-less game card
    """
    def __init__(self, item, item_type):
        self.item = item
        self.type = item_type

    def format(self):
        """
        format the object as a dictionary.
        """
        return {
            "item": self.item,
            "item_type": self.type
        }


class Player(object):
    """
    Player is an external user of the system that will be playing the game
    """
    def __init__(self, username, suspect=None,
                 game_cards=None, card_items_seen=None):
        self.username = username
        if suspect:
            self.suspect = suspect
        else:
            self.suspect = None
        if game_cards:
            self.game_cards = game_cards
        else:
            self.game_cards = list()
        if card_items_seen:
            self.card_items_seen = card_items_seen
        else:
            self.card_items_seen = list()

    def format(self):
        """
        format the object as a dictionary.
        """
        return {
            "username": self.username,
            "suspect": self.suspect,
            "game_cards": [
                game_card.format() for game_card in self.game_cards
            ],
            "card_items_seen": [
                game_card.format() for game_card in self.card_items_seen
            ]
        }
