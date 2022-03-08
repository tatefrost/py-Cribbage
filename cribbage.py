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


def dealCards(player1, player2):
        """Function to deal a hand of cards to the players"""

        deck = Deck()

        deck.shuffle()

        for num in range(0, 6):
                player1.draw(deck)
                player2.draw(deck)

        print("Here is your hand")

        player1.showHand()


def goesFirst(player1, player2):
        """Function to find which player goes first"""

        deck = Deck()

        deck.shuffle()

        player1.draw(deck)
        player2.draw(deck)

        p1card = player1.showHand()
        p2card = player2.showHand()

        if int(p1card[0]) > int(p2card[0]):
                print(f"{player1} goes first")
                return player1
        elif int(p1card[0]) < int(p2card[0]):
                print(f"{player2} goes first")
                return player2
        elif int(p1card[0]) == int(p2card[0]):
                print("It's a tie, re-draw")
                goesFirst()


def startTurn(player):
        """Function which runs each round of play in cribbage"""
        dealCards()

        print(f"Pick a card to put in {player} crib")

        cards = pickCard()


def pickCard():
        """A function that prompts the user to select a card from their hand"""
        pass


def startGame():
        """Function which begins the game"""
        player1 = Player(input("Enter a player name: "))
        player2 = Player("Player2")

        goesFirst(player1, player2)
        startTurn()


def scoreHand():
        """Function which scores a players hand"""
        pass


if __name__ == "__main__":
        startGame()
