#Reid Witte
#using w3schools as a reference

nums = []
once = []

for x in range(10):
    nums.append(int(input("Enter number " + str(x+1) + ": ")))

for x in nums:
    if(nums.count(x) == 1):
        once.append(x)

print("Original List: " + str(nums))
print("Nums that appear once: " + str(once))