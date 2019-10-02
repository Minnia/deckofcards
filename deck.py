# Card game for deck of cards
from random import shuffle
from card import Card


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for value in values for suit in suits]
        # Can also use the method below to append list of card suits and values to self.cards
        # for suit in suits:
        #     for value in values:
        #         self.cards.append(Card(value, suit))

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, number):
        count = self.count()
        smallest_num = min([count, number])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-smallest_num:]
        self.cards = self.cards[:-smallest_num]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self


d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(5)
print(hand)
