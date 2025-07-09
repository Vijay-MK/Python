n= int(input('Enter the a number:'))
a=0
b=1
for i in range(n) :
    c=a+b
    a=b
    b=c

print(f'The value of {n}th element in a Fibonacci series is :{a}')
