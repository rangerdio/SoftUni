start_deck = input().split()
shuffle_times = int(input())

left_slice_deck = start_deck[:len(start_deck) // 2]
right_slice_deck = start_deck[len(start_deck) // 2:]

shuffled_deck = []
for current_shuffle in range(shuffle_times):
    shuffled_deck = []
    for card_index_slice_deck in range(len(left_slice_deck)):
        shuffled_deck.append(left_slice_deck[card_index_slice_deck])
        shuffled_deck.append(right_slice_deck[card_index_slice_deck])

    left_slice_deck = shuffled_deck[:len(start_deck) // 2]
    right_slice_deck = shuffled_deck[len(start_deck) // 2:]

print(shuffled_deck)
