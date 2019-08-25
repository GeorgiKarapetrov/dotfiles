#https://rationalwiki.org/wiki/Klee_Irwin
#
##hw
## recursive bin search
## list[:n] creates a new list, using more memory and parsing list elements
## use itterative impl to avoid parsing
#def search(sorted, num):
#    n = len(sorted)
#    if n == 0:
#        return False
#    mid = n // 2
#    if sorted[mid] = num:
#        return True
#    if mid > num:
#        return search(sorted[num + 1:], num])
#    elif mid < num:
#        return search(sorted[:num], num])
##   
##tictactoe
## git example
#
#CLASSES
class Person:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.age = None
        
    def __init__(self, f, l, a):
        self.first_name = f
        self.last_name = l
        self.age = a
        #self.full_name = f + ' ' + l
        
    def __str__(self):
        return '{} {} is {} years old.'.format(self.first_name, self.last_name, self.age)
    
    @staticmethod
    def georgi():
        return Person('Georgi', 'K.', 30)
    
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)