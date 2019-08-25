#property module
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

if __name__ != '__main__':
    from sys import modules
    self = modules[__name__]
    mod = type(self)
    body = {x: getattr(self, x) for x in dir(self)}
    prop = {k: v for k, v in body.items() if isinstance(v, property)}
    mod = type(mod.__name__, (mod, ), prop)

    self = modules[__name__] = mod(__name__)
    for k, v in {k: v for k, v in body.items() if k not in prop}.items():
        setattr(self, k, v)
