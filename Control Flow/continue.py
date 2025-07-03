#Program is to print all the numbers from 1 to 10 which are not divisible by 3
i=0
while i<10 :
    i+=1
    if i%3 == 0 :
        continue
    print(i)
