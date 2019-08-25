#f_arguments.py
def sum_in_range(a, b):
    return sum(range(a, b + 1))

print(sum_in_range(1, 4))


def test_var_args(*args):
    for arg in args:
        print("arg:{}".format(arg))


def test_var_args(farg, *args):
    print("formal arg:{}".format(farg))
    for arg in args:
        print("another arg:{}".format(arg))


def a(*args):
    print("len of arguments: {0}, arguments: {1}".format(len(args), args))


def sum_numbers(a, b=7):
    return a + b


def tomato(weigth, color='red'):
    print("Tomato - {}gr".format(weigth))
    print("And it is colored {}".format(color))


def test_var_kwargs(farg, **kwargs):
    print("formal arg:{}".format(farg))
    for key in kwargs:
        print ("another keyword arg: {}={}".format(key, kwargs[key]))



def cheeseshop(kind, *args, **kwargs):
    print("-- Do you have any {}".format(kind))

    for arg in args:
        print(arg)

    print("-"*40)

    for key in kwargs:
        print("{}:{}".format(key, kwargs[key]))

cheeseshop("Limburger", "It's very runny, sir.", "It's really VERY runny",
shopkeeper="Michael", client="John", sketch="Cheese Shop Sketch")


