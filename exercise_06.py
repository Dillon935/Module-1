rows, cols = (5,5)
arr = [[0 for i in range(cols)] for j in range(rows)]

row = int(input("Enter a row num from 1 to 5: "))
while not row <= 5 and row >= 1:
    row = int(input("Enter a row num from 1 to 5: "))
col = int(input("Enter a col num from 1 to 5: "))
while not col <= 5 and col >= 1:
    col = int(input("Enter a col num from 1 to 5: "))

arr[row][col] = 1
print('\n'.join(map(str, arr)))