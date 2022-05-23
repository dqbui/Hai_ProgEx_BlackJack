from hashlib import new
from deck import Deck
from hand import Hand


class Game:
    MINIMUM_BET = 1
    BLACK_JACK = 21

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()
        # print(self.deck.cards)

    def start_game(self):
        while self.player.balance > 0:
            game_starter = input(
                f'You are starting with ${self.player.balance}. Would you like to play a hand? ')
            if game_starter.lower() == 'yes':
                while True:
                    try:
                        new_bet = float(input('Place your bet: '))
                        if new_bet > self.player.balance:
                            print('You do not have sufficient funds.')
                        elif new_bet < self.MINIMUM_BET:
                            print('The minimum bet is $1!')
                        else:
                            self.bet = new_bet
                            break
                    except ValueError:
                        print('Invalid! Bet amount must be a number')

                # print(f'Card left in deck {len(self.deck.cards)}')

                player_hand = Hand()
                dealer_hand = Hand()

                player_hand.add_to_hand(self.deck.deal(2))
                dealer_hand.add_to_hand(self.deck.deal(2))

                print(
                    f'Player hand {self.player.get_str_hand(player_hand.cards)}has value {player_hand.get_value()}')
                print(
                    f'Dealer hand {self.dealer.get_str_hand(dealer_hand.cards)}')  # has value {dealer_hand.get_value()}')

                while player_hand.get_value() <= self.BLACK_JACK:
                    hit_or_stay = input(
                        'Would you like to hit or stay? ').lower()

                    if hit_or_stay == 'stay':
                        break
                    elif hit_or_stay == 'hit':
                        player_hand.add_to_hand(self.deck.deal(1))
                        print(
                            f'Player hand {self.player.get_str_hand(player_hand.cards)} has value {player_hand.get_value()}')
                    else:
                        print('That is not a valid option')

                print(
                    f'Final player hand: {self.player.get_str_hand(player_hand.cards)} has value {player_hand.get_value()}')

            else:
                print('Okay then...')

        print(
            'You\'ve ran out of money. Please restart this program to try again. Goodbye.')
