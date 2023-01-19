num = int(input("Enter a number: "))
list = []
for i in range(1,num+1):   
    list.append(float(input("Enter number " + str(i) + ": ")))
print("List: " + str(list))
Average = sum(list) / len(list)
print("Average: " + str(Average))
