PLAYERS = [1,2]
BOARD = [ [ ' ', '_', '_', '_', '_', '_', '_', '_' ], \
          [ '1', '|', ' ', '|', ' ', '|', ' ', '|' ], \
          [ '2', '|', ' ', '|', ' ', '|', ' ', '|' ], \
          [ '3', '|', ' ', '|', ' ', '|', ' ', '|' ], \
          [ ' ', '-', '-', '-', '-', '-', '-', '-' ], \
          [ ' ', ' ', 'A', ' ', 'B', ' ', 'C' ] ]

def printBoard(state):
    for row in state:
        for col in row:
            print(col, end="")
        print()
        
def quitGame(string):
    if string == 'exit':
        quit()