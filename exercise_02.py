#Reid Witte
#using w3schools and geeksforgeekes as a reference

inputOne = input("Enter a string: ")
inputTwo = input("Enter another string: ")

if(len(inputOne) > len(inputTwo)):
    if(inputOne[len(inputOne)-len(inputTwo):] == inputTwo):
        print("True")
    else:
        print("False")
elif(len(inputOne) < len(inputTwo)):
    if(inputTwo[len(inputTwo)-len(inputOne):] == inputOne):
        print("True")
    else:
        print("False")
else:
    print("False")