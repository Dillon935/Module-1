word = input("Enter a string: ")
normal = list(word)
new_list = list()
size = 3

for i in range(0,len(normal), size):
    new_list.append(normal[i:i+size])

print(new_list)