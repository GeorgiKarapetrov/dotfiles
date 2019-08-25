from analizer import * 

def prompt():
    choice = input('Choose a square? eg: 1A: ').lower()
    quit_game(choice)
    try:
        assert len(choice) == 2
        assert int(choice[0]) in (1, 2, 3)
        assert str(choice[1]) in ('a', 'b', 'c')
    except AssertionError:
        print('Only type a single digit and letter. Try again.')
        return prompt()
    return choice.lower()


def play_again(prompt='Wanna play? (y, n): '):
    again = input(prompt)
    if again.lower() == 'y':
        return True
    elif again.lower() == 'n':
        return False
    else:
        print("Enter 'y' or 'n' only.")
        return play_again(prompt)

def play():
    player = 0
    state = init_state

    while has_turn(state):
        print_board(state)
        choice = prompt()
        quit_game(choice)
        state = next_turn(state, choice, player)
        player = next_player(player)
        # we just switched players so the winner would be the previous one
        if has_winner(state):
            print(f'\nNot so bad, player {winner(player)} wins.\n\n')
    

def winner(player):
    if player == 0:
        return 'two'
    else:
        return 'one'
