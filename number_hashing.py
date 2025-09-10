# Python program to demonstrate hashing for finding frequency of a number in array
arr=[]
n=int(input("enter size of array:"))
for i in range(n):
    ele=int(input("enter element:"))
    arr.append(ele)
print("array is:",arr)

max=int(max(arr))

hash_map=[0]*(max+1)

for i in range(n):
    hash_map[arr[i]]+=1

print("hash map is:",hash_map)

a=int(input("enter element whose frequency you want to find:"))
if a>max:
    print("element not found")
else:
    print("frequency of",a,"is:",hash_map[a])

















