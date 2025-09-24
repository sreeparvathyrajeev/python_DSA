# Python program to demonstrate hashing for finding frequency of a lowercase letter in string
s=input("enter a string:")
hash_map=[0]*26
n=len(s)
for i in range(n):
    hash_map[ord(s[i])-ord('a')]+=1
print("hash map is:",hash_map)
a=input("enter a lowercase letter whose frequency you want to find:")

print("frequency of",a,"is:",hash_map[ord(a)-ord('a')])

