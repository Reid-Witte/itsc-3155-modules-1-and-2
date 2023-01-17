#Reid Witte
#using w3schools as a reference

inputString = input("Enter a string: ")
outputList = []
i = 0

for x in inputString:
    if(i % 3 == 0):
        newList = [x]
        outputList.append(newList)
    else:
        temp = outputList[int(i/3)].append(x)
        if(temp != None):
            outputList[int(i/3)] = list(temp)
    i += 1

print(str(outputList))