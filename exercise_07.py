arr = []
num = (input("Enter a number or QUIT to quit: "))
arr.append(num)
while num != "QUIT":
    num = (input("Enter a number or QUIT to quit: "))
    arr.append(num)
arr.remove("QUIT")
print("All Nums: " + str(arr))

print("Even Nums: ")
for num in arr:
    if int(num) % 2 == 0:
        print(num, end=" ")