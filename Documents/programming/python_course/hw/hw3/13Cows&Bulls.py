import random

#make number
def makeNumber():
    digits = set()
    digits.add( random.randint(1,9) )
    while len( digits ) < 4:
        digits.add( random.randint(0,9) )
    
    number = "".join( str( digit ) for digit in digits )
    print(number)
    return number

#check for bulls and cows in an attempt
def play_game( guess, number ):
    bulls = 0
    cows = 0
    
    #look for bulls
    for i,j in zip( guess, number ):
        if i == j:
            bulls = bulls + 1
    
    #look for cows
    for i in range(4):
        for j in range(4):
            if guess[i] == number[j] and i != j:
                cows = cows + 1
                
    print("{} bulls, {} cows".format(bulls, cows) )

#check if all the digits in a guess are distinct
def distinctDigits( string ):
    for i in range(4):
        for j in range(i):
            if string[j] == string[i]:
                print("Choose a number with distinct digits.")
                return True
    return False

def main():
    #start game
    print("Welcome to cows and buls game.")
    
    number = makeNumber()
    
    #counts the number of legal guesses
    counter = 0
    
    #take guess
    while True:
        #except ValueError
        try:
            guess = int( input("What is your guess:") )
            strGuess = str(guess)
        
            #take another guess if the number is not a four digit number
            if len( strGuess ) != 4:
                print("This is not a four digit number.")
                continue
        
            #take another guess if the number has repeating digits
            if distinctDigits(strGuess):
                print("All digits need to be distinct:")
                continue
            
            #play game
            counter = counter + 1
            play_game( strGuess, number )
        
            #stop on win
            if str( guess ) == number:
                print("Congrats, you win. You tried {} times.".format(counter))
                break
    
        except ValueError:
            print("This is not a number. Try again")
            continue
            
main()