#!/usr/bin/python3
from base64 import b32encode

byte_array = '33 46 67 11 7f 47 8e 15 a3 d0 d5 b9 67 f2 73 8b'.split()
byte_string = ''.join(byte_array)
unhexed = byte_string.encode('hex')
key = b32encode(unhexed)
key
