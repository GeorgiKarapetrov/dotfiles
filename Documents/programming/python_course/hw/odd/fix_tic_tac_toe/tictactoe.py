import interaction_dynamics as game

print('Hi, Dummy Bum. Lets play a dummy bum game.')
while game.play_again():
    print("Enter 'exit' to exit")
    game.play()
    continue
print('Thanks, come again.')
