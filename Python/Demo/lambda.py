#lambda is used to make code clean and short
#used when there is one statement

def square(num):
    return num**2

result = square(2)
print(result)

a=lambda x:x**2
print(a(2))

b=lambda y:y+5
print(b(5))
print("--------------------")

mylist=[1,2,3,4,5,6,7,8,8]
list_even = list(filter(lambda x:x%2==0,mylist))
print(list_even)
print("--------------------")

list_power = list(map(lambda x:x**2,list_even))   #map for change(new element) and filter for only filtering the element(same element only filter)
print(list_power)