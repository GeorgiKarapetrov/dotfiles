import copy
import common
import analizer

def prompt():
    choice = input('What do you choose? eg: 1A: ')
    common.quitGame( choice.lower() )

    try:
        assert len(choice) == 2
        assert int(choice[0]) in (1,2,3)
        assert str(choice[1]).lower() in ('a','b','c')
    except AssertionError:
        print('Only type a single digit and letter. Try again.')
        return prompt()
    return choice.lower()


def playAgain(prompt='Do you want to play? (y, n): '):
    again = input(prompt)
    if again.lower() == 'y':
        return True
    elif  again.lower() == 'n':
        return False
    else:
        print("Enter 'y' or 'n' only.")
        return playAgain(prompt)

def play():
    player = 1
    state = copy.deepcopy( common.BOARD )
    
    while analizer.hasTurn(state):
        common.printBoard(state)                
            
        choice = prompt()
    
        common.quitGame( choice )
        
        state = analizer.nextTurn(state, choice, player)
        player = analizer.nextPlayer(player)
    
    if analizer.hasWinner(state):
        print('Congrats, player {} wins.'.format( common.PLAYERS[-player] ) )
    print('Could be worse. Try again.' )