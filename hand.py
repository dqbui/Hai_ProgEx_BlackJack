class Hand:
    def __init__(self):
        self.cards = []
        # self.value = self.get_value()
        # self.cards = ['2s', 'Ah', '3c', 'Ad', '9d', 'Kc']

    def get_value(self):
        hand_value = 0
        ace_count = 0
        for card in self.cards:
            current_val = card[1]  # get value
            if current_val in '23456789':
                hand_value += int(current_val)
            elif current_val == 'A':
                hand_value += 1
                ace_count += 1
            else:
                hand_value += 10

        while hand_value <= 11 and ace_count > 0:
            print('adding in aces')
            hand_value += 10
            ace_count -= 1

        # print(f'Hand value = {hand_value}')

        # self.value = hand_value

        return hand_value

    def add_to_hand(self, new_cards):
        for card in new_cards:
            self.cards.append(card)

    def __str__(self):
        pass


new_hand = Hand()
new_hand.get_value()
