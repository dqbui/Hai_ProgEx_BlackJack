class Dealer:
    def __init__(self):
        pass

    def get_str_hand(self, hand, hidden=False):
        card_str = ''
        if hidden == True:
            card_str = f'{hand[0]}, unknown'
        else:
            for card in hand:
                card_str = card_str + card + ' '

        return card_str

    def hit(self):
        pass
