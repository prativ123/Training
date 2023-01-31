#set are unordered collection of unique element.we can construct them by using set() function.
#set dont have repeated elements, to remove repeated elements in list we convert list to sets.

xyz=set()
#to add to sets add()
xyz.add(1)
xyz.add('hello')
print(xyz)

mylist = ['apple', 'mango', 'orange', 'apple', 'mango', 'orange']
print(mylist)
a=set(mylist)
print(a)