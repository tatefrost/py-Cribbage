"""File for Python cribbage game"""

import random

class Card:
        """Class for single card"""
        def __init__(self, suit, value):
                self.suit = suit
                self.value = value

        def show(self):
                print("{} of {}".format(self.value, self.suit))

        def getValue(self):
                return self.value

        def getCard(self):
                return f"{self.value} of {self.suit}"

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
                self.points = 0
                self.hand = []
    
        def draw(self, deck):
                self.hand.append(deck.drawCard())

                return self

        def removeCard(self, card):
                self.hand.pop(card)

        def showHand(self):
                for card in self.hand:
                        card.show()

                # Usage example ↓

                # deck = Deck()

                # deck.shuffle()

                # bob = Player("Bob")

                # bob.draw(deck)

                # bob.showHand()
        
        def getHand(self):
                hand_cards = []
                for card in self.hand:
                        hand_cards.append(card.getCard())
                return hand_cards

        def points(self, amount):
                self.points += amount

                print(self.points)

                return self.points

        def playCard(self, card):
                cards_played = []


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

        p1card = deck.drawCard()
        p2card = deck.drawCard()


        if (p1card.getValue()) > (p2card.getValue()):
                print(f"{player1.name} goes first")
                return player1, player2
        elif (p1card.getValue()) < (p2card.getValue()):
                print(f"{player2.name} goes first")
                return player2, player1
        elif (p1card.getValue()) == (p2card.getValue()):
                print("It's a tie, re-draw")
                goesFirst(player1, player2)


def startTurn(players):
        """Function which runs each round of play in cribbage"""

        dealCards(players[0], players[1])

        crib = pick2Cards(players[0], players[1])

        deck = Deck()

        deck.shuffle()

        top_card = deck.drawCard()

        playHand(crib, top_card, players)


def pick2Cards(cribPlayer, otherPlayer):
        """A function that prompts the user to select two cards from their hand"""
        
        card1 = input("Pick a card from your hand: ")
        card2 = input("Pick another card from your hand: ")

        crib = []

        i = 0

        for card in cribPlayer.getHand():
                if str(card) == card1 or str(card) == card2:
                        print(f"You selected {card}")
                        crib.append(str(card))
                        cribPlayer.removeCard(i)
                        i -= 1
                i += 1

        j = 0

        for card in otherPlayer.getHand():
                if j < 2:
                        print("Computer has selected a card")
                        otherPlayer.removeCard(j)
                        crib.append(str(card))
                j += 1

        print("Here is your hand:")
        cribPlayer.showHand()

        otherPlayer.showHand()

        print(crib)

        return crib



def startGame():
        """Function which begins the game"""
        player1 = Player(input("Enter a player name: "))
        player2 = Player("Computer")

        startTurn(goesFirst(player1, player2))


def playHand(crib, top_card, players):
        """Function that handles gameplay"""

        play_card = top_card.getValue()

        if play_card == 11:
                players[0].points(2)
                print(f"{players[0].name} gets two points for top card being a Jack")

        print(f"The play card is a {play_card}, {players[0].name} goes first")

        if players[0].name == "Computer":
                computer = players[0]
                player = players[1]
                computer_hand = computer.getHand()
                computer_card = computer_hand[0]
                print(f"The computer chose {computer_card}")
        else:
                player = players[0]
                computer = players[1]
                player.showHand()
                card = input("Choose a card to play: ")








def scoreHand():
        """Function which scores a players hand"""
        pass


if __name__ == "__main__":
        startGame()
