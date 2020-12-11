# Part 2

from random import shuffle as randomShuffle

class Deck:
	def __init__(self):
		suits = ['Hearts','Diamonds','Clubs','Spades'] 
		values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
		self.deck = [c.showCard() for c in [Card(suit, value) for suit in suits for value in values]]

	def deal(self):
		if len(self.deck):
			return ValueError("No cards remaining in deck")
		return self.deck.pop()

	def shuffle(self):
	    if len(self.deck) < 52:
	        return ValueError("Deck is not full, return all cards to shuffle")
	    randomShuffle(self.deck)
	    return self.deck

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def showCard(self):
		return f'{self.value} of {self.suit}'
		
p = Deck()
# print(p.deck)
print(p.shuffle())
