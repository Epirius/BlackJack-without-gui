import Logic


def main():
    num_of_players = 5
    # initializing cards, players and dealer
    cards = Logic.Cards([])
    players = init_players(num_of_players, cards)
    dealer = Logic.Player(cards.deck, "dealer")

    game_turn(cards, players, dealer)
    input("Press any key to exit")
    return


def game_turn(cards, players, dealer):
    new_deck(cards)
    update_deck(cards, players, dealer)

    # deal the starting hand
    dealer.hit_hand()
    for i in players:
        players[i].draw_hand()

    # each player makes their turn
    for i in players:
        hit_or_stand(players[i])
        ace_cleanup(players[i])
        # print(players[i].final_score)
    dealer_turn(dealer)
    # print(dealer.final_score)
    payout(players, dealer)
    return


def hit_or_stand(cur_player):
    while True:
        print()
        print(cur_player.player_id)
        print(cur_player.get_hand())
        print(cur_player.get_score())
        if over_21(cur_player):
            break
        x = input("do you want to hit or stay?: (h/s)")
        if x == 'h':
            cur_player.hit_hand()
        elif x == 's':
            break
        else:
            "invalid input. "
            continue


def ace_cleanup(cur_player):
    x = cur_player.get_score()
    if type(x) == tuple:
        if x[0] > 21:
            x = x[1]
        else:
            x = x[0]
    cur_player.final_score = x


def dealer_turn(dealer):
    while True:
        print()
        print(dealer.player_id)
        print(dealer.get_hand())
        print(dealer.get_score())

        if dealer.get_score() <= 16:
            dealer.hit_hand()
        else:
            ace_cleanup(dealer)
            break


def over_21(cur_player):
    x = cur_player.get_score()
    if type(x) == tuple:
        if x[1] > 21:
            return True
        return False
    else:
        if x > 21:
            return True
        return False


def payout(players, dealer):
    for i in players:
        print()
        print(players[i].player_id + ": " + str(players[i].final_score))
        print(players[i].get_hand())
        if players[i].final_score > 21:
            print(players[i].player_id + ": Bust (over 21)")
            continue
        if dealer.final_score > 21:
            print(players[i].player_id + ": Win (dealer bust)")
            continue
        if dealer.final_score == players[i].final_score:
            print(players[i].player_id + ": Push")
            continue
        if dealer.final_score > players[i].final_score:
            print(players[i].player_id + ": Bust (dealer high)")
            continue
        if dealer.final_score < players[i].final_score:
            print(players[i].player_id + ": Win (dealer low)")
            continue


def init_players(num_players, cards):
    # Use players[i]. to call a player func
    # EX: players[1].draw_hand()
    players = {}
    for i in range(num_players):
        players[i] = Logic.Player(cards.deck, f"player {i}")

    return players


def new_deck(cards):
    cards.generate_deck()
    cards.shuffle()


def update_deck(cards, players, dealer):
    dealer.deck = cards.deck
    for i in players:
        players[i].deck = cards.deck


main()

