
list=[1,2,3,4,5,6,7,8,9,10]
print(min(list)) #to find minimum value
print(max(list)) # to find max value

#random
from random import shuffle
shuffle(list)
print(list)
print("---------------------")
#printing random integer
from random import randint
print(randint(0,100))
print("---------------------")

#'in' operator known as menbership operator
demo=['x','y','z','hello']
print('x' in demo)
print('a' in demo)
print("---------------------")

#'not in' 
print('a' not in demo)
print("---------------------")
# is operator or identity operator
x=10
y=20
z=x
print(id(x))
print(id(y))
print(id(z))

print(x is y)
print(x is z)
print("---------------------")