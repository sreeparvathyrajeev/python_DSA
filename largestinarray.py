
list1=[0]*6
for i in range(6):  
    list1[i]=int(input("enter the number"))
print(list1)

#optimal method to find largest element
def largest():
    l=list1[0]
    for i in range(6):
        if list1[i]>l:
            l=list1[i]
    print("largest element is",l)
largest()
