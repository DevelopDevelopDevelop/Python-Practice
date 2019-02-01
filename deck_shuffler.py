# Build and shuffle a card deck
# My attempt to solve the problem of redundant cards

import random

# Assign list holders
card = []
suit = ["Clubs", "Spades", "Hearts", "Diamonds",]
royals = ["Jack", "Queen", "King", "Ace"]
deck = []

# Create list of numbered cards
for i in range(2,11):
	card.append(str(i))

# Create list of royal cards and Aces
for j in range(4):
	card.append(royals[j])

# Compile deck
for k in range(4):
	for l in range(13):
		cards = (card[l] + " of " + suit[k])

		deck.append(cards)

# Shuffle deck		
random.shuffle(deck)
for m in range(52):
	print(deck[m])
