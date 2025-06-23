#Challenge 1 --> Day number and Day name challenge if day number is 0 then monday and 1 means Tuesday and so on.

dayNo = int(input("Enter the Day number:"))
if dayNo == 0:
    print("Monday")
elif dayNo == 1:
    print("Tuesday")
elif dayNo == 2:
    print("Wednesday")
elif dayNo == 3:
    print("Thursday")
elif dayNo == 4:
    print("Friday")
elif dayNo == 5:
    print("Saturday")
elif dayNo == 6:
    print("Sunday")
else:
    print("Invalid Entry, Please enter day number in the range 0-6")

#Challenge 2 Month number to names ie.. 0--> january 1--> february and so on

monthNo = int(input("Enter the Month number:"))
if monthNo == 0:
    print("Jan")
elif monthNo == 1:
    print("Feb")
elif monthNo == 2:
    print("Mar")
elif monthNo == 3:
    print("Apr")
elif monthNo == 4:
    print("May")
elif monthNo == 5:
    print("June")
elif monthNo == 6:
    print("July")
elif monthNo == 7:
    print("Aug")
elif monthNo == 8:
    print("Sep")
elif monthNo == 9:
    print("Oct")
elif monthNo == 10:
    print("Nov")
elif monthNo == 11:
    print("Dec")
else:
    print("Invalid Entry, Please enter month number in the range 0-11")

#Challange Digit to word
digit = int(input("Enter the digit:"))
if digit == 0:
    print("Zero")
elif digit == 1:
    print("One")
elif digit == 2:
    print("Two")
elif digit == 3:
    print("Three")
elif digit == 4:
    print("Four")
elif digit == 5:
    print("Five")
elif digit == 6:
    print("Six")
elif digit == 7:
    print("Seven")
elif digit == 8:
    print("Eight")
elif digit == 9:
    print("Nine")
else:
    print("Invalid Entry, Please enter month number in the range 0-9")