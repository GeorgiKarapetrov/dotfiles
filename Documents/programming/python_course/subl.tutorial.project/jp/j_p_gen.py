# gen.py

# f() -> __call__

def add1(x, y):
    return x + y

class Add:
    def __call__(self, x, y):
        return x+ y

add2 = Add()

