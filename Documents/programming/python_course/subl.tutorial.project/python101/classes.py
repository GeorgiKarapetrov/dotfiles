class Panda:
    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def _get_buffed(self):
        if self.__weight < 1000:
            self.__weight += 1

    def eat_bamboo(self):
        self._get_buffed()
        return "Nomm nomm nomm!"

    def celebrate_birthday(self):
        self._age += 1

    def __str__(self):
        return "I am a panda - {}".format(self.name)



class Muffin:
    amount = 0
    _e_numbers = ['E500']
    __forbidden_e_numbers = ['E520']

    def __init__(self, color, taste, calories):
        self.color = color
        self.taste = taste
        self.calories = calories
        self._e_numbers = []
        self.__forbidden_e_numbers = ['E102']
        self.__another_private_attr = 'Something'

print(Muffin.__dict__)
print(Muffin._e_numbers)
yummy = Muffin('brown', 'sweet', 420)
print(yummy._Muffin__another_private_attr)
print(yummy.__dict__)
print(yummy._e_numbers)
print(yummy._Muffin__forbidden_e_numbers)



class Worker:
    _hours = 8

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return "Worker's name is: {0}".format(self.name)

    def hours(self):
        return self._hours

class Тailor(Worker):

    def __init__(self, name, address):
        super().__init__(name)
        self.address = address
        
    def get_working_hours(self):
        return self.hours()
        
t = Тailor('Dzuzepe', 'Sofia')
print(t.get_working_hours())
print(t.get_name())



class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = date_as_string.split('-')
        date1 = cls(int(day), int(month), int(year))
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999



