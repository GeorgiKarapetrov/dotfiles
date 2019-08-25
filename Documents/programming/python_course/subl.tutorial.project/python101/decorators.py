#decorators.py
#closure
def get_quadratic_function(a, b, c):

    def quadratic_function(x):
        return a * x ** 2 + b * x + c

    return quadratic_function

func = get_quadratic_function(1, 2, 3)
print(func(1)) # 6
print(func(2)) # 11
print(func(3)) # 18


#decorator
def get_promotion(func):
    def promotion(months, user_id):
        if months >= 3: # 3 is hardcoded
            months += 1
        return func(months, user_id)
    return promotion

@get_promotion
def pay_net(months, user_id):
    print("{} payed Internet for {} months".format(user_id, months))
    save_to_database(months, user_id)

pay_net(5, "radorado@hackbulgaria.com")


#dec2
def get_promotion(promotion_months):
    def accepter(func):
        def decorated(months, user_id):
            if months >= promotion_months:
                months += 1
            return func(months, user_id)
        return decorated
    return accepter

@get_promotion(3)
def pay_net(months, user_id):
    print("{} payed Internet for {} months".format(user_id, months))
    save_to_database(months, user_id)

pay_net(5, "radorado@hackbulgaria.com")
