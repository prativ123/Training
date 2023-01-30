text="Welcome to College"
print(text)
#to count the number of character in the string
print(len(text))
#string indexing
print(text[0])
print(text[0:7])
print(text[7:10])
print(text[:])

#basic string build in methods
#upper(),lower(),split()-> split from every word
print(text.upper())
print(text.lower())
print(text.split())

#formating with placeholder
print("We are here to learn %s programming at %s" %("python","kathford"))