from player import Player
from dealer import Dealer
from game import Game
from time import sleep

STARTING_BALANCE = 500
player = Player(STARTING_BALANCE)
dealer = Dealer()
game = Game(player, dealer)

print("Welcome to Blackjack!")
print()
game.start_game()

print('Program closing in 5 seconds')
sleep(5)
