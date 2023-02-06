#*args -> when the function parameter start with a astrik(*), it allows for number of arguments and function takes them in tuple of values

def demofunction(a,b,c,d,e):
    return a+b+c+d+e


x = demofunction(10,20,30,40,50)
print(x)

def demofunction1(*args):
    return sum(args)

y= demofunction1(10,40,50,60,70,100)
print(y)