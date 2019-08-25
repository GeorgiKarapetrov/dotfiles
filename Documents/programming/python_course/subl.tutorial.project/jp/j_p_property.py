class A:
    def __init__(self, b):
        self._b = b

    @property
    def b(self, value):
        return self._b

    @b.setter
    def b(self, value):
        if value < 0:
            raise ValueError('must be positive')
        self._b = value

if __name__ == '__main__':
    a = A(10)
    print(f'a.b = {a._b}')
    a.b = -100
    print(f'a.b = {a._b}')

