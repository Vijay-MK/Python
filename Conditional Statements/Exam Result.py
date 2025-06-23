#Challenge is to find the identify a student is pass or fail
#min marks is 45 and the max marks is 100
marksinmaths = int(input("Enter your marks in maths:"))
marksinphysics = int(input("Enter your marks in Physics:"))
marksinChemistry = int(input("Enter your marks in Chemistry:"))

if marksinmaths>=45 and marksinphysics>=45 and marksinChemistry>=45 :
    print("Passed")
else:
    print("Failed")

