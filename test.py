list1 = []
for i in range(1,11):
    list1.append(i**2)
print(list1)
print(list1[2:4])
print(list1[:5])
list1.append("pyar is checking if you can add another datatype to a list")
print(list1)
list1.remove("pyar is checking if you can add another datatype to a list")
print(list1)