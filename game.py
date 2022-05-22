from hashlib import new
from deck import Deck
from hand import Hand


class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()

    def start_game(self):
        while self.player.balance > 0:
            game_starter = input(
                f'You are starting with ${self.player.balance}. Would you like to play a hand? ')

            if game_starter.lower() == 'yes':
                while True:
                    new_bet = float(input('Place your bet: '))
                    if new_bet > self.player.balance:
                        print('You do not have sufficient funds.')
                    elif new_bet < 1:
                        print('The minimum bet is $1!')
                    else:
                        self.bet = new_bet
                        break

                print('you lost')
                self.player.balance = self.player.balance - self.bet

            else:
                print('Okay then...')

        print(
            'You\'ve ran out of money. Please restart this program to try again. Goodbye.')
