from hashlib import new
from deck import Deck
from hand import Hand
from time import sleep


class Game:
    MINIMUM_BET = 1
    BLACK_JACK = 21
    HANDS_BEFORE_SHUFFLE = 5

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()
        self.consecutive_hands = self.HANDS_BEFORE_SHUFFLE
        # print(self.deck.cards)

    def start_game(self):
        while self.player.balance > 0:
            game_starter = input(
                f'You are starting with ${self.player.balance}. Would you like to play a hand? ')
            if game_starter.lower() == 'yes':

                self.consecutive_hands -= 1

                if self.consecutive_hands == 0:
                    print('Five hands played. Reshuffling deck')

                    self.deck = Deck()
                    self.consecutive_hands = self.HANDS_BEFORE_SHUFFLE

                while True:
                    try:
                        new_bet = input('Place your bet. Dot (.) for all-in: ')

                        if new_bet == ".":  # all in function
                            print(
                                f'All-in! Player bets ${self.player.balance}')
                            self.bet = self.player.balance
                            break

                        else:  # convert to float and set as bet amount
                            new_bet = float(new_bet)
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
                    f'Dealer hand {self.dealer.get_str_hand(dealer_hand.cards, True)}')  # has value {dealer_hand.get_value()}')

                while player_hand.get_value() <= self.BLACK_JACK:
                    hit_or_stay = input(
                        'Would you like to hit or stay? ').lower()

                    if hit_or_stay == 'stay':
                        print(
                            f'Player hand {self.player.get_str_hand(player_hand.cards)} has value {player_hand.get_value()}')
                        break
                    elif hit_or_stay == 'hit':
                        player_hand.add_to_hand(self.deck.deal(1))
                        print(
                            f'Player hand {self.player.get_str_hand(player_hand.cards)} has value {player_hand.get_value()}')
                    else:
                        print('That is not a valid option')

                if player_hand.get_value() > 21:  # check if bust, if busted then end hand without dealing to dealer
                    print(
                        f'Your hand value is over 21 and you lose ${self.bet} :(')
                    self.player.balance -= self.bet
                else:
                    print('Dealer turn next')
                    print(
                        f'Dealer cards: {self.dealer.get_str_hand(dealer_hand.cards)}')

                    while dealer_hand.get_value() <= self.BLACK_JACK:
                        sleep(1)
                        if dealer_hand.get_value() >= 17:
                            print('Dealer stays')
                            print(
                                f'Dealer hand {self.dealer.get_str_hand(dealer_hand.cards)} has value {dealer_hand.get_value()}')
                            break
                        elif dealer_hand.get_value() <= 16:
                            print('Dealer hits')
                            dealer_hand.add_to_hand(self.deck.deal(1))
                            print(
                                f'Dealer hand {self.dealer.get_str_hand(dealer_hand.cards)} has value {dealer_hand.get_value()}')

                    if dealer_hand.get_value() > 21:
                        print('Player wins')
                        self.player.balance += self.bet

                    else:
                        if dealer_hand.get_value() > player_hand.get_value():
                            print('Dealer wins')
                            self.player.balance -= self.bet
                        elif dealer_hand.get_value() < player_hand.get_value():
                            print('Player wins')
                            self.player.balance += self.bet
                            if player_hand.get_value() == self.BLACK_JACK:
                                print('YOU GOT A BLACKJACK. HALF BET AWARDED')
                                self.player.balance += self.bet/2
                        else:
                            print('Tie')

            else:
                print('Okay then...')

        print(
            'You\'ve ran out of money. Please restart this program to try again. Goodbye.')
