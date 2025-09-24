#sliding window algorithm

def subarray(arr,k):
    n = len(arr)
    if n<k:
        return "invalid k"
    min_sum=float('inf')
    min_subarray=[]
    for i in range(n-k+1):
        current_sum=sum(arr[i:i+k])
        if current_sum < min_sum:
            min_sum=current_sum
            min_subarray=arr[i:i+k]
    return min_subarray

