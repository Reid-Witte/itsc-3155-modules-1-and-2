#Reid Witte
#using w3schools as a reference

grade = int(input("Enter a grade from 0 to 100: "))

letterGrade = "F"

if(grade > 89):
    letterGrade = "A"
elif(grade > 79):
    letterGrade = "B"
elif(grade > 69):
    letterGrade = "C"
elif(grade > 59):
    letterGrade = "D"

print("Your grade is " + letterGrade)