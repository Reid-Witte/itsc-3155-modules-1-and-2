#Reid Witte
#using w3schools as a reference

numListOne = []
numListTwo = []
outputList = []

for x in range(5):
    numListOne.append(int(input("Enter a number for the first list: ")))

for x in range(5):
    numListTwo.append(int(input("Enter a number for the second list: ")))

print("First List: "+ str(numListOne))

print("Second List: "+ str(numListTwo))

for x in numListOne:
    if(numListTwo.count(x) > 0 and outputList.count(x) == 0):
        outputList.append(x)

print("Common List: "+ str(outputList))