n= 5
max = 0
i=0
print('Enter',n,'Numbers:')
while i<5 :
    x= int(input())
    if x > max :
        max = x
    i+=1
print('Max = ', max)