class Player:
    def __init__(self, balance):
        self.balance = balance

    def get_str_hand(self, hand):
        card_str = ''
        for card in hand:
            card_str = card_str + card + ' '

        return card_str
