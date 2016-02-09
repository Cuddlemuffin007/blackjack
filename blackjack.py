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
        self.cards = []

    def __str__(self):
        return "hand containing: " + ' '.join([str(card) for card in self.cards])

    def add_card(self, card):
        self.cards.append(card)


class Player:

    def __init__(self):
        self.player_id = "Player"
        self.hand = Hand()

    def __str__(self):
        return "{} has ".format(self.player_id) + str(self.hand)


class Dealer(Player):

    def __init__(self):
        self.player_id = "Dealer"
        self.hand = Hand()


class Game:

    VALUES = {
            'A': 1, '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'J': 10, 'Q': 10, 'K': 10
            }

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def get_hand_value(self, hand):
        total = 0
        for card in hand:
            total += self.VALUES[card.get_rank()]
        return total
