# time complexity O(n^2)
def selectionsort(arr):
    for count in range(len(arr)):
        lowest=count
    
        for i in range(count,len(arr)):
            if arr[i]<arr[lowest]:
                lowest=i
        temp=arr[count]
        arr[count]=arr[lowest]
        arr[lowest]=temp
    
    return arr
