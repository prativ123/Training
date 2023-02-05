#nested loop:loop inside loop

color=['white','red','black','orange','blue']
fruits=['apple','orange','mango','banana']


for looks in color:
    for name in fruits:
        print(looks,name)

#range
for x in range(10):
    print(x)
print("------------")

for y in range(10,20):
    print(y)
print("------------")

#break

for z in range(21,30):
    if z == 25:
        break #ends after condition meets
    print(z)
print("------------")
#continue
for z in range(21,30):
    if z == 25:
        continue  #skips 25 and then continues the loop,if condition met skips the condition.
    print(z)
print("------------")