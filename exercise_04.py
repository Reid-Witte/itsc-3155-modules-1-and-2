#Reid Witte
#using w3schools as a reference

n = int(input("Enter a number: "))
numList = []
sum = 0.0

for x in range(n):
    numList.append(float(input("Enter number: ")))
    sum += numList[x]

print("List: " + str(numList))
print("Average: " + str(sum/len(numList)))
