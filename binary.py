__author__ = 'charan'

from struct import *

# Store as bytes data
packed_data = pack('iif', 6, 19, 4.73)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# To get bytes data back to normal (b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@')
original_data = unpack('iif', packed_data)
print(original_data)
print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))


# ---------- Binary AND -----------

a = 50      # 110010
b = 25      # 011001
c = a & b   # 010000
print(c)

# ----------- Binary Right Shift ----

x = 240     # 11110000
y = x >> 2  # 00111100
print(y)