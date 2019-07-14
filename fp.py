# %%

import struct

def q4_4(num):
    return struct.unpack('b', bytes([num]))[0] / 2**4

def q8_8(num):
    return struct.unpack('h', struct.pack('h', num))[0] / 2**8

def q16_16(num):
    return struct.unpack('i', struct.pack('i', num))[0] / 2**16

def convert(num):
    return q16_16(num)

# assert q34(0b00000000) ==  0.0
# assert q34(0b00010000) ==  1.0
# assert q34(0b00100000) ==  2.0
# assert q34(0b00110000) ==  3.0
# assert q34(0b01000000) ==  4.0
# assert q34(0b00001000) ==  0.5
# assert q34(0b11110000) == -1.0

# a = 0b11100000;
# b = 0b00101000;
# c = a * b

# print(format(a, '08b'))
# print(q34(a))

# print(format(b, '08b'))
# print(q34(b))

# print(format(c, '016b'))
# print(q78(c))

# result = (c & (0xFF << 4)) >> 4
# print(format(result, '08b'))
# print(q34(result))

# comp = (~result & 0xFF) + 1
# print(format(comp, '08b'))
# print(q34(comp))

# print(convert(1 << 16))
# print(convert(1 << 7))  # dt = 2e-9 ~= 0.00195 ms
print(convert(0b00000000000000010000000000000000))
print(convert(0b00000000000000101011001011011010))

