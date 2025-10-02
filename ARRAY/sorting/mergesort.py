#time complexity: O(n log n)

def mergesort(arr):
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]
    sorted_left = mergesort(left_half)
    sorted_right = mergesort(right_half)
    return merge(sorted_left, sorted_right) if len(arr) > 1 else arr
def merge(left,right):
    sorted_arr = []
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted_arr.append(left[i])
            i+=1
        else:
            sorted_arr.append(right[j])
            j+=1
    #append remaining elements
    #only one the lists will have remaining elements
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr
