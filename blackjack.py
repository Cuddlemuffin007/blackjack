# tiy blackjack oop project
import random


class Card:

    SUITS = ('H', 'S', 'C', 'D')
    RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{}{}".format(self.rank, self.suit)

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank


class Deck:

    def __init__(self):
        self.deck = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]

    def __str__(self):
        return "Deck contains: " + ' '.join([str(card) for card in self.deck])

    def shuffle(self):
        return random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()


class Hand:

    def __init__(self):
        self.hand = []

    def __str__(self):
        return "Hand contains: " + ' '.join([str(card) for card in self.hand])

    def add_card(self, card):
        self.hand.append(card)
