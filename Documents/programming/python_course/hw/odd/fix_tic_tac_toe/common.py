BOARD = """
       ___________
    1 | {} | {} | {} |
       -----------
    2 | {} | {} | {} |
       -----------
    3 | {} | {} | {} |
       -----------
        A   B   C
    """
init_state = [' '] * 9


def print_board(state):
  print(BOARD.format(*state))


def quit_game(string):
  if string == 'exit':
    quit()
