#how to find the binary format of a number using format()
a=10
print(format(a,'b'))
#also we can use bin()

a=15
print(bin(a))

#to find the bit length we can use variable.bit_length()

a = 25
print(a.bit_length())

a = 10
b = 13
print(10 & 13)
print(format(8,'b'))

print(a | b)
print(format(15,'b'))

print(a^b)
print(format(7,'b'))
print(a)
print(a<<1)
print(a<<2)
print(a<<5)

print(a)
print(a>>1)
print(a>>2)
print(a>>5)

print(~a)