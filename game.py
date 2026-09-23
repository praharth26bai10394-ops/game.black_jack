from deck import Deck


S = input("Type T to start the game: ")

if S.upper() == "T":

    deck = Deck()
    deck.shuffle()

    # Player cards
    player_cards = []
    player_cards.append(deck.deal_card())
    player_cards.append(deck.deal_card())

    # Banker cards
    banker_cards = []
    banker_cards.append(deck.deal_card())
    banker_cards.append(deck.deal_card())

    print("\n--- NEW GAME ---")

    print("Your cards are:", player_cards[0], "and", player_cards[1])
    print("Banker shows:", banker_cards[0], "and [Hidden Card]")

    # Calculate player's total
    player_total = 0

    for card in player_cards:

        if card.rank == "J" or card.rank == "Q" or card.rank == "K":
            player_total = player_total + 10

        elif card.rank == "A":
            player_total = player_total + 11

        else:
            player_total = player_total + int(card.rank)

    if player_total == 22:
        player_total = 12

    print("Your total is:", player_total)

    # Player's turn
    while player_total < 21:

        ctu = input("Hit, Stand, OR Double? ").lower()

        if ctu == "hit":

            card = deck.deal_card()
            player_cards.append(card)

            print("\nYou drew:", card)

            if card.rank == "J" or card.rank == "Q" or card.rank == "K":
                player_total = player_total + 10

            elif card.rank == "A":
                player_total = player_total + 11

            else:
                player_total = player_total + int(card.rank)

            if player_total > 21 and card.rank == "A":
                player_total = player_total - 10

            print("Your new total is:", player_total)

        elif ctu == "stand":

            break

        elif ctu == "double":

            card = deck.deal_card()
            player_cards.append(card)

            print("\nYou doubled down!")
            print("You drew:", card)

            if card.rank == "J" or card.rank == "Q" or card.rank == "K":
                player_total = player_total + 10

            elif card.rank == "A":
                player_total = player_total + 11

            else:
                player_total = player_total + int(card.rank)

            if player_total > 21 and card.rank == "A":
                player_total = player_total - 10

            print("Your final total is:", player_total)

            break

        else:

            print("Invalid input. Please type Hit, Stand, or Double.")

    # Check player's result
    if player_total > 21:

        print("\nBust! You went over 21. Banker wins.")

    else:

        print("\nBanker reveals hidden card:", banker_cards[1])

        # Calculate banker's total
        banker_total = 0

        for card in banker_cards:

            if card.rank == "J" or card.rank == "Q" or card.rank == "K":
                banker_total = banker_total + 10

            elif card.rank == "A":
                banker_total = banker_total + 11

            else:
                banker_total = banker_total + int(card.rank)

        if banker_total == 22:
            banker_total = 12

        # Banker's turn
        while banker_total < 17:

            card = deck.deal_card()
            banker_cards.append(card)

            print("Banker hits and draws:", card)

            if card.rank == "J" or card.rank == "Q" or card.rank == "K":
                banker_total = banker_total + 10

            elif card.rank == "A":
                banker_total = banker_total + 11

            else:
                banker_total = banker_total + int(card.rank)

            if banker_total > 21 and card.rank == "A":
                banker_total = banker_total - 10

        print("Banker's final total is:", banker_total)

        # Final result
        if banker_total > 21:

            print("\nBanker busts! You win!")

        elif player_total > banker_total:

            print("\nYou win!")

        elif banker_total > player_total:

            print("\nBanker wins!")

        else:

            print("\nIt's a tie (Push)!")


else:

    print("Game Did Not Start")