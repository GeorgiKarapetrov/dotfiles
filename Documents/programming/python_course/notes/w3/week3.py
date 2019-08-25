##local and global var; run debugger
#a = 5
#def f():
#    a = 10
#    print(a)
#    def inner():
#        global a
#        print(a)
#        def innerIN():
#            a = 20
#            print(a)
#        def nonLocal():
#            nonlocal a
#            print(a)
#        
#    inner()
#    innerIN()
#    nonLocal()
#    
#print(a)
#f()
#print(a)
#
##var space
#del a
#del f

#numPy, Panda, Jupiter

##2.26.2019

#tuples
##immutable (like strings)
#t = (1, 2, 3)
##sequence unpacking
#(a, b, c) = [1,2,3]
#a, b, c = t
#for x in t:
#    print(x)
##multiple assignment
#a, b, c = 1,2,3
#multiple return
#def f():
#    return 5, "bla"
#print(f())

#sets
#s1 = {1,2,3,3}
#
#2 in s1 #boolean
##binary search
#20 in s1 #works for lists
#l = [1,2,3,4,5]
#s2 = set(l)
#set() #empty set
#{} # empty dict
#union = s1 | s2
#intersect = s1 & s2
#s1 - s2
#complimentOfIntersect = s1 ^ s2
#s1.add(5)
#for x in s1:
#    print(x)
#    
#{str(x) for x in l}
##no tupple comprehension, generator expression
#(str(x) for x in l)
#
##cannot add list or set or other immutables to set, add tupple or frosen set
#s1.add( (6,7,8) )
#s1.add( frozenset({9,10}) )
#
##dict
#dict1 = {'dog' : 'куче', 'cat' : 'котка' }
#dict1['dog']
#dict1['mouse'] = 'мишка'
#dict1['mouse']
#dict1.values()
#dict1.keys()
#dict1.items()
#dict1.get()
#d2 = dict()
#dict1.update(d2)



#example
YEARS = {
    'Isaac Newton' : 1642,
    'Marie Curie' : 1867,
    'Albert Einstein' : 1879,
    'Guido van Rossum' : 1956
    }

def getYear(person):
    return YEARS.get(person)


#dict comp
l = list(range(30))
def dictify(l):
    d = {}
    for x in l:
        d[x] = str(x)
    return d
#alternatively
{x : str(x) for x in l}
#one element tuple
t = (1,)
t = 1,










#string.replace(token, token)
#sum(list)