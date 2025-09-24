list1=[9789,4,3,5,4,9]

for count in range(len(list1)):
    lowest=count
    
    for i in range(count,len(list1)):
        if list1[i]<list1[lowest]:
            lowest=i
    temp=list1[count]
    list1[count]=list1[lowest]
    list1[lowest]=temp
    
print(list1)
