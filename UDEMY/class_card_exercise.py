import random


class Card:
    allowed_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    allowed_value = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self, suit, value):
        if suit not in Card.allowed_suits and value not in Card.allowed_value:
            raise ValueError("Error")
        self.suit=suit
        self.value=value
        
    def __repr__(self):
        return self.value + " of " + self.suit
        
class Deck:
    def __init__(self):
        self.cards = [Card(i,j) for i in Card.allowed_suits for j in Card.allowed_value]
    
    def count(self):
        return len(self.cards)

    def __repr__(self):
        return "Deck of " + str(self.count()) + " cards"

    def _deal(self, n):
        if self.count()==0:
            raise ValueError("All cards have been dealt")
        else:
            print("a")
            removed = self.cards[-n:]
            self.cards = self.cards[:-n]
            if len(removed) == 1:
                return removed[0]
            return removed
    
    def shuffle(self):
        if self.count() != len(Card.allowed_suits) * len(Card.allowed_value):
            raise ValueError("Only full decks can be shuffled")
        return random.shuffle(self.cards)

    def deal_card(self):
        x=self._deal(1)
        return x

    def deal_hand(self,n):
        return self._deal(n)