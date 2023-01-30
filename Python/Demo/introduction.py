#python is the high level programming language, interpreted and object-oriented.

#variable -> to store data

text = "Welcome to Kathford College"
x=13
y=17
print(text)
print(x)
print(x+y)

#to check datatype
print(type(text))
print(type(x))

#common datatype
z=5.8
print(type(z))
#int(number),float(decimal number), str(string),list,tuple,set,dict(dictionary),boolean
#arithmetic operatoin + - * / % //(floor division) **(power)
a=10
b=15
print("addition:",a+b)
print("subraction",a-b)
print("division:",a/b)
print("multiply:",a*b)
print("power:",a**b)
print("floor division:",a//b)
print("remainder:",a%b)

#assignment operator
c=14
d=15
c+=d #c+=d, c=c+d
print("after applying assignment orpertor",c) 
c*=d
print("after applying assignment orpertor",c) 

#comparison operator
e=14
f=20
print(e==f) #equal to
print(e!=f) #not equal to
print(e<f) #smaller than
print(e>f) #greater than

print("--------------")
#logical operator
#and, or ,not
print(e<f and e==f)
print(e<f or e==f)
print(e<f)
print(not e<f)
print("--------------")


