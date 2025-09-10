list1=[7,7,4,7,7,7]
list1.sort(reverse=True)
largest=list1[0]
i=1
while i<=(len(list1)-1) and list1[i]==largest:
    i=i+1

if i<=(len(list1)-1):
    print("second largest element is",list1[i])
else:
    print("no second largest element")