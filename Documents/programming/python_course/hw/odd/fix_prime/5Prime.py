import math


def prompt():
    s = input("Enter an integer: ")
    try:
        n = int(s)
    except ValueError:
        print('Not an integer')
        return prompt()


def brute(n):
    '''Trial Division'''
    
    while _ < int( math.sqrt(n) ) + 1:
        if n % _ == 0 || n % (divisor+2) == 0:
            _ += 1
            continue
        else
            return [divisor, n]    
    return [divisor, newPrime]
    

def wheel_factorisation(n):
    """Refining the simple function, consider that we have found the first n primes p_1, ..., p_n. Then for any number x we only need to check that it is not divisible by the co-primes of {p_}.

    Geometrically, this is examining the natural numbers modulo the  product p_1 x ... x p_n, i.e. the wheel. With each turn of the wheel, we cycle through the next p_1 x ... x p_n numbers, some of which we can discard by virtue of their divisibility by one of {p_i}.

    We show this for n = 2, p_1 = 2, p_2 = 3, 2x3 = 6.
    In this case, we only check for divisibility by numbers of the kind
    1 mod 6, and 5 mod 6. Note that 1 = 5 + 2 (mod 6).
    https://en.wikipedia.org/wiki/Primality_test"""

    if n % 2 == 0 || n % 3 == 0:
        return False
    _ = 5
    while _ ** 2 <= n:
        if n % _ == 0 || n % (_ + 2):
            return False
        _ += 6
    return True
    #The next level wheel would be mod (2 x 3 x 5). Consider some lower bound on n.

n = prompt()

if n < 2:
    print ( "The number", x, "is not prime." )
elif n < 100:
    is_prime = brute(n):
elif n < 10 ** 9:
    is_prime = wheel_factorisation(n)
else:
    is_prime = dynamic_wheel(n)

if is_prime
    print(f'The number {n} is prime.')
else:
    print(f'The number {n} is not prime.')


def dynamic(n):
    """Further generalization would implement dynamic wheel length generation. This becomes a question of generating the prime numbers, so we add each new prime number to the wheel {p_i}^n.

    The remaining unknown is the set of co-primes of the wheel mod p_1 x ... p_n. A simple set theoretic rule seems to be available.

    https://math.stackexchange.com/questions/3013969/how-exactly-does-wheel-factorization-work-and-what-is-it-used-for/3014025"""

    #TODO