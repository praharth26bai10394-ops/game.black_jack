import random


def card_value(card):

    if card.rank == "A":
        return 11

    elif card.rank == "K" or card.rank == "Q" or card.rank == "J":
        return 10

    else:
        return int(card.rank)


def calculate_score(cards):

    score = 0
    ace_count = 0

    for card in cards:

        score = score + card_value(card)

        if card.rank == "A":
            ace_count = ace_count + 1

    while score > 21 and ace_count > 0:

        score = score - 10
        ace_count = ace_count - 1

    return score


def show_cards(cards):

    for card in cards:
        print(card.rank, "of", card.suit)


def draw_card(deck):

    position = random.choice(range(len(deck.cards)))

    card = deck.cards.pop(position)

    return card


def player_turn(deck, player_cards):

    while True:

        print("\nYour cards:")
        show_cards(player_cards)

        score = calculate_score(player_cards)

        print("Your score:", score)

        if score > 21:

            print("You went over 21.")
            break

        choice = input("Do you want another card? (yes/no): ")

        if choice == "yes":

            card = draw_card(deck)
            player_cards.append(card)

        elif choice == "no":

            break

        else:

            print("Please enter yes or no.")


def dealer_turn(deck, dealer_cards):

    print("\nDealer's turn")

    while calculate_score(dealer_cards) < 17:

        card = draw_card(deck)
        dealer_cards.append(card)

    print("\nDealer's cards:")
    show_cards(dealer_cards)

    print("Dealer's score:", calculate_score(dealer_cards))


def find_winner(player_cards, dealer_cards):

    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    print("\n========== RESULT ==========")

    if player_score > 21:

        print("Dealer wins.")

    elif dealer_score > 21:

        print("Player wins.")

    elif player_score > dealer_score:

        print("Player wins.")

    elif dealer_score > player_score:

        print("Dealer wins.")

    else:

        print("It is a draw.")




# Testing Module 3

# from deck import Deck

# deck = Deck()

# player_cards = []

# player_cards.append(draw_card(deck))
# player_cards.append(draw_card(deck))

# print("Player cards:")
# show_cards(player_cards)

# print("Player score:", calculate_score(player_cards))

# print("Cards remaining in deck:", len(deck.cards))