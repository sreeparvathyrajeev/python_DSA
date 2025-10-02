def lowerbound(arr,target):
    left=0
    right=len(arr)-1
    result=len(arr)
    
    while left<=right:

        mid=(left+right)//2
        if arr[mid]>=target:
            result=mid
            right=mid-1
        else:
            left=mid+1
    return result
