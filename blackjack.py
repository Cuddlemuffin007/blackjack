# tiy blackjack oop project
from sys import exit
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

    def show_hand(self):
        return "{} has: ".format(self.player_id) + ' '.join([str(card) for card in self.hand.cards])


class Dealer(Player):

    def __init__(self):
        self.player_id = "Dealer"
        self.hand = Hand()

    def show_hand(self):
        return "{} shows: ".format(self.player_id) + 'X ' + ' '.join([str(card) for card in self.hand.cards[1:]])


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
        self.player_bust = False
        self.dealer_bust = False

    def get_hand_value(self, hand):
        total = 0
        has_ace = False
        for card in hand:
            total += self.VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                has_ace = True

        if has_ace and total < 12:
            total += 10

        return total

    def player_turn(self):
        prompt = "{} ({}). You can (h)it or (s)tand.\n>> "

        print("{}".format(self.dealer.show_hand()))

        if self.get_hand_value(self.player.hand.cards) == 21:
            print('Blackjack! You win!', self.player.hand)
            return True

        while True:
            choice = input(prompt.format(self.player.show_hand(), self.get_hand_value(self.player.hand.cards))).lower()
            if choice == 'h':
                self.player.hand.add_card(self.deck.deal_card())
                print(self.player.show_hand())
                if self.get_hand_value(self.player.hand.cards) > 21:
                    self.player_bust = True
                    return True
            elif choice == 's':
                print("You stand on {}".format(self.get_hand_value(self.player.hand.cards)))
                return False

    def dealer_turn(self):

        if self.get_hand_value(self.dealer.hand.cards) == 21:
            return True

        while True:
            if self.get_hand_value(self.dealer.hand.cards) >= 17:
                return True
            while self.get_hand_value(self.dealer.hand.cards) < 17:
                self.dealer.hand.add_card(self.deck.deal_card())
                if self.get_hand_value(self.dealer.hand.cards) > 21:
                    self.dealer_bust = True
                    return True

    def play_again(self):

        play = input("Deal again?\n>> ").lower()
        if play == 'y':
            new_game = Game()
            new_game.deal()
        elif play == 'n':
            print("See you later!")
            exit(0)

    def deal(self):
        hand_over = False

        self.deck.shuffle()
        self.player.hand.add_card(self.deck.deal_card())
        self.dealer.hand.add_card(self.deck.deal_card())
        self.player.hand.add_card(self.deck.deal_card())
        self.dealer.hand.add_card(self.deck.deal_card())

        hand_over = self.player_turn()
        if not hand_over:
            self.dealer_turn()

        form = (self.player.show_hand(), str(self.dealer))

        if self.player_bust:
            print("{}\n{}\nPlayer bust! You lose!".format(form[0], form[1]))
        elif self.dealer_bust:
            print("{}\n{}\nDealer bust! You win!".format(form[0], form[1]))
        elif self.get_hand_value(self.player.hand.cards) == self.get_hand_value(self.dealer.hand.cards):
            print("{}\n{}\nIt's a draw! You still lose though...".format(form[0], form[1]))
        elif self.get_hand_value(self.player.hand.cards) > self.get_hand_value(self.dealer.hand.cards):
            print("{}\n{}\nYou win!".format(form[0], form[1]))
        else:
            print("{}\n{}\nYou lose!".format(form[0], form[1]))

        self.play_again()


game = Game()
game.deal()
