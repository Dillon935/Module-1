arr = []
for i in range (10):
    num = int(input("Enter number " + str(i) + ": "))
    arr.append(num)
print("Orginal List:" + str(arr))
n = len(arr)
arr.sort()
print("Nums that appear once: ")
if arr[0] != arr[1]:
        print(arr[0], end = " ")
for i in range(1, n - 1):
        if (arr[i] != arr[i + 1] and
            arr[i] != arr[i - 1]):
            print( arr[i], end = " ")
if arr[n - 2] != arr[n - 1]:
        print(arr[n - 1], end = " ")
