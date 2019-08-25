#https://www.youtube.com/watch?v=BRn6UCw35og
# look at property.py and module_property.py
def f(x=[]):
    x.append(len(x))
    return x

print(f'f() = {f()}')
print(f'f() = {f()}')
print(f'f() = {f()}')


def f(x=None):
    if x == None:
        x = []
    x.append(len(x))
    return x

print(f'f() = {f()}')
print(f'f() = {f()}')
print(f'f() = {f()}')


def f(*args, **kwargs):
    def f(x=[]):
        x.append(len(x))
        return x
    return f(*args, **kwargs)

print(f'f() = {f()}')
print(f'f() = {f()}')
print(f'f() = {f()}')
