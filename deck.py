from cards import Card


class Deck:

    def __init__(self):

        self.cards = []

        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for suit in suits:

            for rank in ranks:

                self.cards.append(Card(suit, rank))


# Testing Module 2

# deck = Deck()
# print("Number of cards:", len(deck.cards))