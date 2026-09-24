class Player:

    def __init__(self, name):

        self.name = name
        self.cards = []

    def show_cards(self):

        for card in self.cards:
            print(card.rank, "of", card.suit)

    def add_card(self, card):

        self.cards.append(card)


# Testing Module 4

# from deck import Deck

# deck = Deck()

# player = Player("Praharth")

# player.add_card(deck.cards.pop())
# player.add_card(deck.cards.pop())

# print("Player name:", player.name)

# print("Player cards:")
# player.show_cards()