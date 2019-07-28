# %%
# back-of-the-envelope fixed point stuff

import struct

def q4_4(num):
    return struct.unpack('b', bytes([num]))[0] / 2**4

def q8_8(num):
    return struct.unpack('h', struct.pack('h', num))[0] / 2**8

def q16_16(num):
    return struct.unpack('i', struct.pack('i', num))[0] / 2**16

def convert(num):
    return q16_16(num)

# sanity check
assert q4_4(0b00000000) ==  0.0
assert q4_4(0b00010000) ==  1.0
assert q4_4(0b00100000) ==  2.0
assert q4_4(0b00110000) ==  3.0
assert q4_4(0b01000000) ==  4.0
assert q4_4(0b00001000) ==  0.5
assert q4_4(0b11110000) == -1.0

# verifying results from verilog simulation
print(convert(1 << 16))
print(convert(1 << 7))  # dt = 2e-9 ~= 0.00195 ms
print(convert(0b00000000000000010000000000000000))
print(convert(0b00000000000000101011001011011010))

