#Boolean Datatype
a = True
b = True
c = a + b
print(c) #output is 2 we will get integer as output

b = False

c = a + b
print(c) #output is 1 we will get integer as output

c = a - b
print(c) #output is 1 we will get integer as output

c = a * b
print(c) #output is 0 we will get integer as output

#c = a / b
print(c) #output is error (Zero Division error)

#c = a // b
print(c) #output is error (Zero Division error)

b = True
c = a / b
print(c) #Output is 1.0

c = a // b
print(c) #output is 1

#Complex Datatypes
#all the Arithmetic Operator expect floor division (//) and Modulus (%)
a1 = 3 + 2j
a2 = 9 + 8j
c1 = a1 + a2
print("The sum of the given 2 complex number is:", c1) # Output = (12 + 10j)

c1 = a1 - a2
print("The difference of the given 2 complex number is:", c1) #output = (-6 - 6j)

c1 = a1 * a2
print("The multiplication of the given 2 complex number is:", c1) #output = (27 + 16j)

c1 = a1 / a2
print("The Division of the given 2 complex number is:", c1) #output = (0.296551724137931-0.04137931034482758j)