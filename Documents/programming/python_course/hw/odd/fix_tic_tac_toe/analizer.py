from common import * 
CHOICES = '1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c'
SIGNS = {0: 'X', 1: 'O'}
LEGAL_WINS = [
    # horizontals
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    # verticals
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    # diagonals
    [0, 4, 8],
    [2, 4, 6],
    ]


def next_turn(state, choice, player):
    i = CHOICES.index(choice)
    if state[i] == ' ':
        state[i] = SIGNS.get(player)
    else:
        print('This square is taken. Try again.')
    return state


def next_player(player):
    if player == 0:
        return 1
    return 0


def has_turn(state):
    if has_winner(state):
        print_board(state)
        return False
    for _ in state:
        if _ == ' ':
            return True
    return False


def has_winner(state):
    for conf in LEGAL_WINS:
        is_win = state_wins(conf, state)
        if is_win:
            return is_win
    return False

def state_wins(conf, state):
    if state[conf[0]] == ' ':
        return False
    return state[conf[0]] == state[conf[1]] == state[conf[2]]
