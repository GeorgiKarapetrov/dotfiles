#import pudb
#pudb.set_trace()

def getInt(prompt='Enter a number:'):
    while True:
        s = input(prompt)
        n = int (s)
        return n
    
def getTwoInt():
    i1= getInt()
    i2= getInt()
    return i1, i2

try:
    x,y = getTwoInt()
except ValueError:
    print("This is not an integer.")
else:
    result = x*y
    print('{} * {} = {}'.format(x,y,result) )
