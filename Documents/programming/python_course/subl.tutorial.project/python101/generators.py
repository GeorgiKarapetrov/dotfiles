#generators.py
#lists
frameworks = ['django', 'angular', 'rails']
frameworks.append(frameworks)

frameworks[-1] is frameworks
print(frameworks)


#iterator
class MyIterator:
    def __init__(self):
        self.index = 0
        self.data = [1, 2, 3]

    def __iter__(self):
        return self

    def __next__(self):
        index = self.index
        self.index += 1

        try:
            return self.data[index]
        except IndexError:
            raise StopIteration


#fibo
class FibUpTo:
    def __init__(self, up_to):
        self.up_to = up_to
        self.num = 0
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.up_to:
            raise StopIteration

        if self.num < 2:
            self.num += 1
            return 1
        self.a, self.b = self.b, self.a + self.b
        self.num += 1
        return self.b

fib = FibUpTo(10)

for number in fib:
    print(number)


#generator
def degrees(number):
    i = 2

    while i < 5:
        yield number ** i

        i += 1
        print(i)

degrees = degrees(2)
for degree in degrees:
    print(str(degree) + "\n")


#fibo gen
def fib():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b

for f in fib():
    print(f)


#complex gen
def complex_generator():
    print('Hey I just met you')

    items = [1, 2, 3]

    for item in items:
        print('And this is crazy')

        wtf = (yield item)

        print(wtf)

    print('But here is my number.')
    print('So call me maybe.')

    return 42


