#Challenge is if temp = 25 --> Normal temp<25 --> cold temp>25 --> Hot
#Using the nested if
temp = float(input("Enter the temperature:"))
if temp == 25.0 :
    print("Normal")
else:
    if temp < 25.0 :
        print("Cold")
    else:
        print("Hot")


#Challenge solved using the elif

temp = float(input("Enter the temperature:"))
if temp == 25.0 :
    print("Normal")
elif temp < 25.0 :
        print("Cold")
else:
        print("Hot")