#largest element in array
list1=[0]*6
for i in range(6):  
    list1[i]=int(input("enter the number"))
print(list1)
def largest():
    l=0
    for i in range(6):
        if list1[i]>list1[l]:
            l=i
    print("largest element is",list1[l])
largest()