import random

#first prompt
while True:
    number = random.randint(1,9)
    g =  input("Enter a number: ")
    if g == "exit":
        break
    
    #game prompt
    while True:
        if g == "exit":
            break
        
        guess = int(g)
        
        if guess == number:
            g = input( "Succes.")
            break
        
        elif number > guess:
            g = input( "Try bigger:") 
            continue
        
        elif number < guess:
            g = input( "Try smaller:") 
            continue
