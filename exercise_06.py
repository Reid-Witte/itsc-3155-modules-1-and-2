#Reid Witte
#using w3schools as a reference

rowNum = int(input("Enter a row num from 1 to 5: "))
colNum = int(input("Enter a col num from 1 to 5: "))

grid = ""

for x in range(5):
    for y in range(5):
        if(x == rowNum-1 and y == colNum-1):
            grid += "1 "
        else:
            grid += "0 "
    grid += "\n"

print(grid)