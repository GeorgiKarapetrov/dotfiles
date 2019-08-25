from common import PLAYERS as players
from common import printBoard

CHOICES = '1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c'
TRANSLATIONS = (1,2), (1,4), (1,6), (2,2), (2,4), (2,6), (3,2), (3,4), (3,6)
DICT = { choice:translation for choice, translation in zip(CHOICES, TRANSLATIONS) }
SIGNS_DICT = { players[0] : 'X' , players[1] : 'O' }


def nextTurn(state, choice, player):
    i,j = DICT.get(choice)
    if state[i][j] == ' ':
        state[i][j] = SIGNS_DICT.get(player)
    else:
        print('This square is taken. Try again.')
    return state


def nextPlayer(player):
    if player == players[0]:
        return players[1]
    else:
        return players[0]


def hasTurn(state):
    if hasWinner(state):
        printBoard(state)
        return False

    for box in TRANSLATIONS:
        i,j = box
        if state[i][j] == ' ':
            return True

    return False


def hasWinner(state):
    for conf in conf_generotor(state):
        if confWins(conf, state):
            return confWins(conf, state)
    return False


def conf_generotor(state):
    rows = [ TRANSLATIONS[:3], TRANSLATIONS[3:6], TRANSLATIONS[6:] ]
    cols = [[rows[i][j] for i in range(3)] for j in range(3)]
    mainDiag = [ [ rows[0][0], rows[1][1], rows[2][2] ] ]
    antiDiag = [ [ rows[0][2], rows[1][1], rows[2][0] ] ]
    legalWins = rows + cols + mainDiag + antiDiag

    return legalWins


def confWins(conf, state):
    if state[ conf[0][0] ][ conf[0][1] ]  != 'X' and state[conf[0][0]][conf[0][1]] != 'O':
        return False
    
    symbols = []
    for el in conf:
        symbols.append( state[el[0]][el[1]] )
    return symbols[0] == symbols[1] and symbols[1] == symbols[2]
