from deck import Deck
from player import Player
from dealer import Dealer
from game import draw_card, player_turn, dealer_turn, find_winner, calculate_score


print("========== BLACKJACK ==========")

name = input("Enter your name: ")

deck = Deck()

player = Player(name)
dealer = Dealer()


# Initial cards

player.add_card(draw_card(deck))
player.add_card(draw_card(deck))

dealer.deal_card(deck)
dealer.deal_card(deck)


# Player turn

print("\nYour turn")
player_turn(deck, player.cards)


# Dealer turn

if calculate_score(player.cards) <= 21:
    dealer_turn(deck, dealer.cards)


# Find winner

find_winner(player.cards, dealer.cards)