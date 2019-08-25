# dec.py

def log(f):
    def logged(x, y):
        rv = f(x, y)
        print(f.__name__, x, y, '->', rv)
        return rv
    return logged

@log
def add(x, y):
    '''add two thins'''
    return x + y

add = log(add)

print('1 + 2 = ', add(1, 2))

