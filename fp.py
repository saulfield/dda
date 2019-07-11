# %%

import struct

def q34(num):
    return struct.unpack('b', bytes([num]))[0] / 2**4

def q78(num):
    return struct.unpack('h', struct.pack('h', num))[0] / 2**8

assert q34(0b00000000) ==  0.0
assert q34(0b00010000) ==  1.0
assert q34(0b00100000) ==  2.0
assert q34(0b00110000) ==  3.0
assert q34(0b01000000) ==  4.0
assert q34(0b00001000) ==  0.5
assert q34(0b11110000) == -1.0

a = 0b00110100
b = 0b00100001
c = a * b

print(format(a, '08b'))
print(format(b, '08b'))
print(format(c, '016b'))
print(q78(c))

result = (c & (0xFF << 4)) >> 4
print(format(result, '08b'))
print(q34(result))
