#CLASSES
#stick to API conventions
class Mamal():
    def __init__(self, k = 'generic'):
        self.kind = k
        
#old
class Person(Mamal):
    n_hands = 2
        
    def __init__(self, f='', l='', a=0):
        self.first_name = f
        self.last_name = l
        self.age = a
    
    @staticmethod
    def georgi():
        return Person('Georgi', 'K.', 30)
    
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def __str__(self):
        return '{} is {}'.format(self.full_name(), self.age)
    
e = Person('evgeni', 'pandurski', 40)
g = Person.georgi()

#new again
#sub class
class SuperPerson( Person ):
    def __init__(self, person: Person=Person().georgi(), p=''):
        super().__init__(person.first_name, person.last_name, person.age)
        self.power = p
        
    def __str__(self):
        return '{} and has {}.'.format(super().__str__(), self.power)
    
    
print( str( SuperPerson( g, 'power' ) ) )

m = Mamal()
h = Person
print( isinstance(h, Mamal) )
print( isinstance(m, Mamal) )
print( issubclass(Person, Mamal) )
print( issubclass(Person, Person) )

#application
#distance ex
#hw implement freest space
    