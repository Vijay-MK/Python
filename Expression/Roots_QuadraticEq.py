from math import sqrt
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
print("Your Quadratic equation is:",a ,"X^2 + ", b, "X + ",c , "=0")
if (((b*b)-(4*a*c)) < 0) :
    print("The value is complex")
else:
    r1 = ((-1 * b) + sqrt((b * b) - (4 * a * c))) / (2 * a)
    r2 = ((-1 * b) - sqrt((b * b) - (4 * a * c))) / (2 * a)
    print("The roots of the above quadratic equation are: ", r1,"and ", r2)

