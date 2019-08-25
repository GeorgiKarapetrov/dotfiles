#context_man.py
#general
class some_context_manager:
    def __enter__(self):
        # set things up
        return self

    def __exit__(self, type, value, traceback):
        # tear things down
        pass

with some_context_manager() as thing:
     # some code
     pass


#specific
class Log:
    def __init__(self, filename):
        self.filename = filename
        self.file_handler = None

    def log(self, text):
        self.file_handler.write(text + '\n')

    def __enter__(self):
        print('__enter__')
        self.file_handler = open(self.filename, 'r+')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        self.file_handler.close()

with Log('log_file.txt') as logger:
    print('In with block')
    logger.log('Some log')
    logger.log('Another log')

with Log('log_file1.txt') as l1:
    l1.log('In file 1')

    with Log('log_file2.txt') as l2:
        l2.log('In file 2')


#context lib
from contextlib import contextmanager

@contextmanager
def open_file(filename):
    file_handler = open(filename)

    yield file_handler

    file_handler.close()

with open_file('some_file.txt') as f:
    print(f.read())

#cont lib 2
@contextmanager
def context_manager():
    print('Entering')
    try:
        yield 'Yielded value'
        print('Exiting successfully')
    except Exception as exc:
        print('Excepting..', exc)
    finally:
        print('Finally..')

with context_manager() as cm:
    print('Inside context manager')
    print('Return value of context manager: ', cm)

    raise Exception('Smt went wrong.')

