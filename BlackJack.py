import Logic


def main():
    print("\n" * 50)
    num_of_players = 2
    # initializing cards, players and dealer
    cards = Logic.Cards([])
    players = init_players(num_of_players, cards)
    dealer = Logic.Player(cards.deck, "dealer")
    global rounds_played
    rounds_played = 0
    update(cards, num_of_players, players, dealer)
    #game_turn(cards, players, dealer)


def update(cards, num_of_players, players, dealer):
    while True:
        global rounds_played
        # get a new deck and shuffle it every 7 turns.
        if rounds_played > 7 or rounds_played < 1:
            new_deck(cards)
            update_deck(cards, players, dealer)
            rounds_played = 0
        rounds_played += 1
        clear_hands(players, dealer)

        # deal the starting hand
        dealer.hit_hand()
        for i in players:
            players[i].draw_hand()

        print("\n" * 2)
        if input("Do you want to quit? (y/n): ") in ('y', 'Y', 'yes', 'YES', 'Yes'):
            print("\n" * 50)
            return

        for i in range(num_of_players + 1):
            if i < num_of_players:

                # taking bets
                while True:
                    print("\n" * 50)
                    bet = int(input(
                        f'{players[i].player_id} you have {players[i].money} dollars, how much would you like to bet?: '))
                    if bet <= 0 or bet > players[i].money:
                        print('Invalid amount')
                    else:
                        players[i].money -= bet
                        players[i].bet = bet
                        break
                # player turn
                hit_or_stand(players[i], dealer)
                ace_cleanup(players[i])

            else:
                # this is the dealers turn
                print("\n" * 50)
                dealer_turn(dealer)
                payout(players, dealer)


def hit_or_stand(cur_player, dealer):
    while True:
        print("\n" * 50)
        print(dealer.player_id)
        print(dealer.get_hand())
        print(dealer.get_score())
        print("\n" * 5)
        print(cur_player.player_id)
        print(cur_player.get_hand())
        print(cur_player.get_score())

        if over_21(cur_player):
            input('Press any key to continue')
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
            print(f'amount lost is: {players[i].bet}')
            print(f'Current amount is: {players[i].money}')
            players[i].bet = 0
            continue
        if dealer.final_score > 21:
            print(players[i].player_id + ": Win (dealer bust)")
            players[i].money = players[i].money + players[i].bet * 2
            print(f'amount won is: {players[i].bet}')
            print(f'Current amount is: {players[i].money}')
            players[i].bet = 0
            continue
        if dealer.final_score == players[i].final_score:
            print(players[i].player_id + ": Push")
            players[i].money = players[i].money + players[i].bet
            players[i].bet = 0
            print(f'Current amount is: {players[i].money}')
            continue
        if dealer.final_score > players[i].final_score:
            print(players[i].player_id + ": Bust (dealer high)")
            print(f'amount lost is: {players[i].bet}')
            print(f'Current amount is: {players[i].money}')
            players[i].bet = 0
            continue
        if dealer.final_score < players[i].final_score:
            print(players[i].player_id + ": Win (dealer low)")
            players[i].money = players[i].money + players[i].bet * 2
            print(f'amount won is: {players[i].bet}')
            print(f'Current amount is: {players[i].money}')
            players[i].bet = 0
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


def clear_hands(players, dealer):
    dealer.hand = []
    for i in players:
        players[i].hand = []


main()
