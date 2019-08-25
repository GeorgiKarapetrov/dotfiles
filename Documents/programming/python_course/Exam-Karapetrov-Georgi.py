# Exam
# Introduction to Programming with Python
# Evgeni Pandurski, Progress

# Problem 1
def sqrt1(x: float):
    try:
        return x ** 2
    except TypeError:
        print(f'{x} is not a number')


# Promblem 2
def nums_div_by_x_and_not_div_by_y(x=7, y=5, start=2000, end=3200):
    result = []
    for _ in range(start, end + 1):
        if _ % x == 0 and _ % y != 0:
            result.append(_)
    print(
        f'The numbers between  and {start} and {end} divisible by {x} but not by {y} are:\n{result}')
# nums_div_by_x_and_not_div_by_y()


# Problem 3
def sort_words(prompt='Enter some words separated by spaces: '):
    words = str(input(prompt))
    # exclude repeating words with (set)
    list_o_words = list(set(words.split()))
    # lexicographical order
    print(sorted(list_o_words))
# sort_words()


# Problem 4
class Recrangle:
    def __init__(self, x: int, y: int):
        try:
            assert x > 0 and y > 0
            self.x = x
            self.y = y
        except AssertionError:
            print('Both the length and width need to be positive.')
            raise AssertionError
    def area(self):
        return self.x * self.y


# Problem 5
class American:
    def __init__(self):
        print('Murica')
class NewYorker(American):
    def __init__(self):
        print('Yankee Doodle Do')


# Problem 6
def dev_by_nill(x=5):
    return x / 0
def context(dev):
    try:
        dev()
    except ZeroDivisionError:
        print(f'5 не се дели на 0.')
#context(dev_by_nill)


# Problem 7
def char_counter(prompt='Enter a string: '):
    string = str(input(prompt))
    chars = [char for char in string]
    counter = {}
    for _ in chars:
        if counter.__contains__(_):
            counter.__setitem__(_, counter.get(_) + 1)
        else:
            counter.__setitem__(_, 1)
    for _ in (counter):
        print(f'{_}, {counter.get(_)}')
#char_counter()


# Problem 8
def weird_sum(prompt='Enter a one digit number: '):
    while True:
        string = input(prompt)
        try:
            assert len(string) == 1
            num = int(string)
        except AssertionError:
            print('Only one symbol, please.')
            continue
        except ValueError:
            print('Enter a number, please.')
            continue
        break
    print(f'{num + (10 * num + num) + (100 * num + 10 * num + num) + (1000 * num + 100 * num + 10 * num + num)}')
#weird_sum()


# Bonus
import re
def pass_regex(prompt='Enter a password: '):
    passwd = input(prompt)
    try:
        assert 6 <= len(passwd) <= 20
        # no white spaces:
        assert len(passwd.split()) == 1
        assert re.match('\d+', passwd)
        assert re.match('[a-z]+', passwd)
        assert re.match('[A-Z]+', passwd)
        assert re.match('\W+', passwd)
        print('You password is valid.')
    except AssertionError:
        print("Your password is not valid.")
#pass_regex()