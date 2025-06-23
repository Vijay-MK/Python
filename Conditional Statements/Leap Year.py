#challenge is the find the input year is leap year or not.
#Julian Calender
print("Julian Calender")
year = int(input("Enter the year:"))
if year %4 == 0 :
    print("Leap Year")
else:
    print("Non-Leap Year")

#Grigorean Calender
print("Grigorean calander")
year = int(input("Enter the year:"))
if year % 100 == 0 :
    if year % 400 == 0:
        print("Leap Year")
    else:
        print("Not a Leap Year")
elif year % 4 == 0 :
    print("Leap Year")
else:
    print("Not a Leap Year")