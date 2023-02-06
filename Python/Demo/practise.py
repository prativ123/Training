
#checking number of vowels in a sentense
text="Hello World"  
c=0
for check in text:
    if check in "aeiou":
        c=c+1      
print(c)  
print("------------------")
    
#10 natural number
for num in range(1,11):
    print(num)
print("------------------")

#multiply all element in the list
mylist=[1,2,3,4,5]
a=1
for num in mylist:
    a=a*num
print(a)
print("------------------")

#multiply all element in the list excluding one number every time
mylist=[1,2,3]
newlist=[]
a=1
for num in mylist:
    a=a*num
    
print(a)

for num in mylist:
    newlist.append(a//num)
print(newlist)
print("------------------")
print("------------------")

#palindrome 
text="madam"
x=text[::-1] #reverses the text
if text==x:
        print("Palindrome")
else:
        print("not palindrome") 
print("------------------")
print("------------------")

#armstrong number


# x=371
# result=0

# while x != 0 :
#        remainder = x % 10
#        result += remainder * remainder * remainder
#        x /= 10
# if result == x:
#      print("armstrong number")
# else:
#      print("not armstrong number")


r,p = 371,371
result = 0
while p!=0:    
    remainder= p%10
    result += remainder**(3)
    p//=10

print(result)
if result == r: 
     print("yes")
else: 
     print("no")

