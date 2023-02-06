#filter is built in function used to filter out the item.

mylist=[1,2,3,4,5,6,7,8,9,10]

def check_even(num):
    return num%2==0

newlist=list(filter(check_even,mylist))

print(newlist)