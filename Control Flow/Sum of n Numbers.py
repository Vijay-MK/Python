#Challenge is to add a list of numbers and store it in the sum
sum = 0
i=0
list = [1,5,10,18]
while i < len(list) :
    sum += list[i]
    i+=1
print("Sum of the list of numbers is:",sum)

#Sum of n numbers
sum = 0
n= 5
i=0
while i<=n :
    sum += i
    i+=1
print('The sum of numbers is:',sum)

#Sum of 5 numbers from the input of users
sum = 0
i=0
print('Enter 5 Numbers:')
while i<5 :
    x=int(input())
    sum+=x
    i+=1
print('sum=', sum)




