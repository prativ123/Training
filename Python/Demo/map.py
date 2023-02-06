#map() applies a given function to each element of

def square(num):
    return num**2


numbers=[2,3,4,5,6,7,8]
testresult = list(map(square,numbers))
print(testresult)