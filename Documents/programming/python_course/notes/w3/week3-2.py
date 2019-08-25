##file reading
##os.listdir()
#f = open('file', 'r')
#lines = f.readlines()
#records = [l.split('regex') for l in lines]
##when line is split in two
#dict = {record[0] : int(record[1]) for record in records}
#print(dict)
#    

#catch
def catch():
    while True:
        s = input('asdasd:')
        try:
            return int(s)
        except ValueError:
            print('Not number.')
            continue
        except ZeroDivisionError:
            print("Devide by 0")
            continue
print(catch())


#catch2
import pudb
pudb.set_trace()

def getInt(prompt='Enter a number'):
    while True:
        s = input(prompt)
        n = int (s)
        return n
    
def getTwoInt():
    i1
    i2
    return

try:
    x,y = getTwoInt()
except ValueError:
    print()
else:
    result = x*y
    print('{x} * {y} = {result}'.format(x,y,result)
          
#hw 12, 13, 14, 15