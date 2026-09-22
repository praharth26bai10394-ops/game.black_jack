from deck import Deck


def calculate_score(cards):
    score = 0
    aces = 0

    for card in cards:
        if card.rank == "J" or card.rank == "Q" or card.rank == "K":
            score += 10
        elif card.rank == "A":
            score += 11
            aces += 1
        else:
            score += int(card.rank)

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score


def show_cards(cards):
    for card in cards:
        print(card)


def play_game():
    deck = Deck()
    deck.shuffle()

    player_cards = []
    dealer_cards = []

    player_cards.append(deck.deal_card())
    player_cards.append(deck.deal_card())

    dealer_cards.append(deck.deal_card())
    dealer_cards.append(deck.deal_card())

    print("\n===== BLACKJACK =====")

    print("\nYour cards:")
    show_cards(player_cards)

    print("Your score:", calculate_score(player_cards))

    print("\nDealer's first card:")
    print(dealer_cards[0])

    while calculate_score(player_cards) < 21:

        choice = input("\nDo you want another card? (yes/no): ")

        if choice.lower() == "yes":
            player_cards.append(deck.deal_card())

            print("\nYour cards:")
            show_cards(player_cards)

            print("Your score:", calculate_score(player_cards))

        else:
            break

    player_score = calculate_score(player_cards)

    if player_score > 21:
        print("\nYou went over 21!")
        print("Dealer wins.")
        return

    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deck.deal_card())

    dealer_score = calculate_score(dealer_cards)

    print("\nDealer's cards:")
    show_cards(dealer_cards)

    print("Dealer's score:", dealer_score)

    print("\n===== RESULT =====")

    if dealer_score > 21:
        print("Dealer went over 21!")
        print("You win!")

    elif player_score > dealer_score:
        print("You win!")

    elif player_score < dealer_score:
        print("Dealer wins!")

    else:
        print("It's a tie!")


play_game()

# testing the game module

# deck = Deck()

# print("Number of cards:", len(deck.cards))

# deck.shuffle()

# print("First card:", deck.deal_card())
# print("Cards remaining:", len(deck.cards))