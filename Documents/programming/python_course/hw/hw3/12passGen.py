import string
import random

chars = string.ascii_letters + string.digits + string.punctuation

while True:

    try:
        strenght = int( input("Enter your password's lenght:") )
        break
    except ValueError:
        print("This is not an integer.")
        continue

print( "".join(random.sample(chars, strenght) ) )
