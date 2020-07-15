import random

num_decks = 4  # ammount of decks used

class Cards():

    def __init__(self, deck):
        self.deck = deck

    def generate_deck(self):
        self.deck = []
        for i in range(num_decks):
            for i in ['H', 'D', 'S', 'C']:
                self.deck.append('A' + i)
                for j in range(2, 14):
                    self.deck.append(str(j) + i)
        return self.deck

    def shuffle(self):
        return random.shuffle(self.deck)

    def draw(self):
        x = self.deck[0]
        del self.deck[0]
        return x


class Player():

    def __init__(self, deck, player_id):
        self.hand = []
        #self.handgui = []
        self.deck = deck
        self.player_id = player_id
        self.final_score = -1
        self.money = 500
        self.bet = 0

    # draw 2 hands first time
    def draw_hand(self):
        self.hit_hand()
        self.hit_hand()

    # get a single card
    def hit_hand(self):
        x = self.deck[0]
        del self.deck[0]
        self.hand.append(x)

    def get_hand(self):
        return self.hand

    def get_score(self):
        self.score = []
        for i in range(len(self.hand)):
            x = list(self.hand[i])  # sets x to a card
            del x[-1]  # removes the suit from the card
            if x in (['1', '1'], ['1', '2'], ['1', '3']):  # set value of face cards to 10
                x = ['1', '0']
            self.score.append("".join(x))

        if 'A' not in self.score:
            return sum([int(x) for x in self.score])

        elif 'A' in self.score:
            A_amount = self.score.count('A')
            for i in range(A_amount):
                del self.score[self.score.index('A')]
            x = sum([int(x) for x in self.score])
            if self.player_id == "dealer":
                return (x + (11 * A_amount))
            return (x + (11 * A_amount), x + (1 * A_amount))
