
a = input("Insert a Value : ")
print("You Insert " + str(a))
a = a.replace('.', '')

print(a)
print("Value Inserted is numeric: " + str(a.isnumeric()))