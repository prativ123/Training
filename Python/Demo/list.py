#list are similar to array in other programming language and 
#list are mutable ie elements inside list can be changed.

fruits=['apple','banana','orange','mango']
print(fruits)
print(fruits[0])
print(fruits[1:3])
#append -> to add new element in the list
fruits.append('papaya')
print(fruits)

#pop() -> remove element from the list,by default it will remove the last 
# element but to remove from specific position we use indexing

fruits.pop()
print(fruits)
fruits.pop(1)
print(fruits)
#len()-> to count number of element in the list
#clear()-> clearall elements from the list
#extend()-> to extend two list
#sort()-> rearrange the elements in the ascending order
#reverse()-> rearrange the elements in the reverse order.
print(len(fruits))
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.extend(["kiwi","cherry"])
print(fruits)
fruits.clear()
print(fruits)