import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        self.cards = self.shuffle()
        # print(self.cards)
        # print(len(self.cards))

    def create_deck(self):
        self.cards = []
        card_list = []
        for suit in Card.SUIT_SYMBOLS.values():
            # print('suit:', suit)
            for num in Card.VALUE_NAMES.values():
                # print('value:', num)
                # print(suit + num)
                card_list.append(suit + num)

        # print(card_list)
        # print(len(card_list))
        return card_list

    def shuffle(self):
        print('shuffling')
        random.shuffle(self.cards)
        return self.cards

    def deal(self, num_cards):
        cards_dealt = []
        for _ in range(num_cards):
            cards_dealt.append(self.cards.pop(0))
            print('Dealt a card')
        return cards_dealt


# new_deck = Deck()
# print(len(new_deck.cards))
# new_deck.deal(2)
# print(len(new_deck.cards))
# new_deck.deal(2)
# print(len(new_deck.cards))
# new_deck.deal(2)
# print(len(new_deck.cards))
# new_deck.deal(2)
# print(len(new_deck.cards))
