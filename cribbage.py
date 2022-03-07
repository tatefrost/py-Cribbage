"""File for Python cribbage game"""

import random

class Card:
    """Class for single card"""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value, self.suit))

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
        for card in self.cards:
            card.show()

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
        self.hand.append(deck.drawCard())

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


def dealCards():
        """Function to deal a hand of cards to the players"""
        pass


def startTurn():
        """Function which runs each round of play in cribbage"""
        dealCards()


def pickCard():
        """A function that prompts the user to select a card from their hand"""
        pass


def startGame():
        """Function which begins the game"""
        startTurn()


def scoreHand():
        """Function which scores a players hand"""
        pass


if __name__ == "__main__":
        startGame()
