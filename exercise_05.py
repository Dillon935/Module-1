num1 = int(input("Enter a number for the first list: "))
num2 = int(input("Enter a number for the first list: "))
num3 = int(input("Enter a number for the first list: "))
num4 = int(input("Enter a number for the first list: "))
num5 = int(input("Enter a number for the first list: "))
list_1 = [num1,num2,num3,num4,num5]
num_1 = int(input("Enter a number for the second list: "))
num_2 = int(input("Enter a number for the second list: "))
num_3 = int(input("Enter a number for the second list: "))
num_4 = int(input("Enter a number for the second list: "))
num_5 = int(input("Enter a number for the second list: "))
list_2 = [num_1,num_2,num_3,num_4,num_5]

print("First List: " + str(list_1))
print("Second List: " + str(list_2))

list_3 = set(list_1) & set(list_2)
print("Third List: " + str(list_3))
