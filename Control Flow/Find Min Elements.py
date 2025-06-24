n= 5
min = 0
i=0
print('Enter',n,'Numbers:')
while i<5 :
    x= int(input())
    if x < min :
        min = x
    i+=1
print('Min = ', min)