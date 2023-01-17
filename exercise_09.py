#Reid Witte
#using w3schools as a reference

words = []

for x in range(5):
    words.append(input("Enter a word: "))

print("Words: " + str(words))

stringOut = ""

for x in words:
    stringOut += x + " "

print("One String: " + stringOut)