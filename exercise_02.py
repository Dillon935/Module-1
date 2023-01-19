s1 = input("Enter a String: ")
s2 = input("Enter another String: ")

result = s2.endswith(s1)
result2 = s1.endswith(s2)

if(result or result2):
    print("True")
else:
    print("False")