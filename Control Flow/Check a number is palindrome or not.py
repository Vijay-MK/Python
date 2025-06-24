n = int(input('Enter a Number:'))
rev = 0
number=n
while n>0 :
    r=n%10
    rev = (rev*10) + r
    n = n//10

print('Reverse:', rev)

if (rev == number) :
    print('The Entered number is Palindrome')
else:
    print('Not Palindrome')