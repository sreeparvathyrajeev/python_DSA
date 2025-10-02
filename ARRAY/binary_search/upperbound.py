def upperbound(arr,target):
    left=0
    right=len(arr)-1
    result_index=len(arr)
    while left<=right:
        mid=(left+right)//2
        if arr[mid]<=target:
            left=mid+1
        else:
            result_index=mid
            right=mid-1
    return result_index