#chellenge is that in a store the discount is given with respect to the total bill amount
# ie.. bill amount < 1000 then 10% bill amount > 1000 and < 5000 then 15 % or if bill amount > 5000 then 25%
amount = float(input("Enter your Bill amount:"))
if amount < 1000 :
    amount -= amount*0.10
    print("You have got 10 % discount and your final Bill amount is ", amount)
elif amount >= 1000 and amount< 5000 :
    amount -= amount * 0.15
    print("You have got 15 % discount and your final Bill amount is ", amount)
else:
    amount -= amount * 0.25
    print("You have got 25 % discount and your final Bill amount is ", amount)