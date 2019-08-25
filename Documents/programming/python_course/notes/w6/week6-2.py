#algorithms
# stable, adaptive, in-place, almost in place, 
#sum_0^n -> O(1)
def sum(n: int):
    return n*(n+1)/2

#binary search -> time: O(log_2(n))
#              -> space: O(n) (recusion generates new lists)
#              -> space: O(log(n)) itterative impl

#sort
#merge -> time: O(n*log_2(n))
#quick -> time: O(n*log_2(n))
#heap  -> time: O(n*log_2(n)) in-place
#tim   -> time: O(n*log_2(n)) adaptive

def comparator(tupple):
    return tupple[1], tupple[0]

sorted(list, key=comparator)

sorted(list, key=lambda tupple: tupple[1], tupple[0])

#finding bottlenecks
from timeit import timeit
timeit('1+1')
timeit('int("1")+int("1")')

import datetime
def time():
    i = datetime.datetime
    def f():
        pass
    f = datetime.datetime
    return f - i

@time
def f():
    pass



#data structures
#doubly linked list, tuple, set, dict, class, stack, que (heap), (binary) tree, graph, (deque, heapq - add quickly in front and at end)
#hw - 19, loot at hangman (examples)
#prosti chisla, implement distance in cortyard, re-write tica tac