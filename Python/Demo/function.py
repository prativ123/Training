#function is block of code which can be called which performs particular task.
# runs after being called. 
# it can be reused

#to define a function 
def demoFunction():
    print("Welcome to Hell")

demoFunction()

#return function for assigning value.

def add_num():
    return 10+20

result= add_num()
print(result)

def mul_num(a,b):
    return a*b

a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
mult= mul_num(a,b)

print(mult)
