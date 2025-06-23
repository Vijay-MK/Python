#Chaining Comparison
a=10
b=5
c=3
print(a>b and b>c)
print(a>b>c)
d=6
print(a>b and b>c and c<d)
print(a>b>c<d)

#is Operator
# to find the id of an variable we can use id(variable_name)
a= 10
b=a
print(a is b)

x= 25
y = 25
print ("x=", id(x),"y=",id(y))
print(x is y)

a= 'Hello'
b= 'Hello'
print ("a=", id(a),"b=",id(b))
print(a is b)
