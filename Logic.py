import random


class Cards():

    def __init__(self, deck):
        self.deck = deck

    def generate_deck(self):
        self.deck = []
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
            x = list(self.hand[i])
            del x[-1]
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