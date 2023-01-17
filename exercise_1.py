#Reid Witte
#using w3schools as a reference

stringInput = input("Enter a string: ")
stringOutput = ""

for x in stringInput:
    if(x == x.lower() and x != " "):
        stringOutput += x

for x in stringInput:
    if(x != x.lower() and x != " "):
        stringOutput += x

print(stringOutput)