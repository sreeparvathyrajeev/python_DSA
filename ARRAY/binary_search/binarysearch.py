#arr is a sorted array
#returns the index of target if found else returns -1
def binarysearch(arr,target):
    left = 0
    right = len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
