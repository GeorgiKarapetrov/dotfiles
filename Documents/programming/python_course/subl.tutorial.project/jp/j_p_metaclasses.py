class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if 'baz' not in body:
            raise TypeError()
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def __init__(self):
        pass
    def bar(self):
        return self.baz()

#at user side (in another file)
class Derived(Base):
    def __init__(self):
        super(Derived, Base).__init__()
    def baz(self):
        return 'baz'


