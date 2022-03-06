"""File for Python cribbage game"""

import random

class Card:
    """Class for single card"""
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print("{} of {}".format(self.val, self.suit))

class Deck:
    """Class for a deck"""
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def show(self):
        for c in self.cards:
            c.show()

            # Usage example ↓

            # deck = Deck()

            # deck.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)

            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

            # Usage example ↓

            # deck = Deck()

            # deck.shuffle()

            # deck.show()

    def drawCard(self):
        return self.cards.pop()

        # Usage example ↓

        # deck = Deck()

        # deck.shuffle()

        # card = deck.drawCard()

        # card.show()

class Player:
    """Class for a player"""
    def __init__(self, name):
        self.name = name
        
        self.hand = []

        def draw(self, deck):
            self.hand.append(deck.drawcard())

            return self

        def showHand(self):
            for card in self.hand:
                card.show()

                # Usage example ↓

                # deck = Deck()

                # deck.shuffle()

                # bob = Player("Bob")

                # bob.draw(deck)

                # bob.showHand()
