from deck import Deck


class Dealer:

    def __init__(self):
        self.cards = []

    def deal_card(self, deck):
        card = deck.deal()
        self.cards.append(card)

    def show_cards(self):
        print("Dealer cards:")

        for card in self.cards:
            print(card)


# Testing code

# deck = Deck()
# dealer = Dealer()

# dealer.deal_card(deck)
# dealer.deal_card(deck)

# dealer.show_cards()