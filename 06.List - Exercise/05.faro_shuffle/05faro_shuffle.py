initial_deck = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    deck_middle = int(len(initial_deck) / 2)
    left_cards = initial_deck[:deck_middle]
    right_cards = initial_deck[deck_middle:]

    current_deck = []
    for card_index in range(len(left_cards)):
        current_deck.append(left_cards[card_index])
        current_deck.append(right_cards[card_index])
    initial_deck = current_deck

print(initial_deck)

