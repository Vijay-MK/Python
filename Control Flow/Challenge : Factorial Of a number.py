n = int(input("Enter an number:"))
factorial = 1
for i in range(1,n+1):
    factorial *=i
print(f'The factorial of {n}! is : {factorial}')