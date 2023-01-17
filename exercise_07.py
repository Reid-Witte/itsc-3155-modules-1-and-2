#Reid Witte
#using w3schools as a reference

allNums = []
evenNums = []

while True:
    num = input("Enter a number or QUIT to quit: ")
    if(num == "QUIT"):
        break
    allNums.append(int(num))
    if(int(num) % 2 == 0):
        evenNums.append(int(num))

print("All Nums: " + str(allNums))
print("Even Nums: " + str(evenNums))