#brute
indexpairs=[]
def twosum(nums,target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                indexpairs.append((i,j))
    return indexpairs
    

if __name__=="__main__":
    nums=[2,4,5,3,4,7]
    target=8
    print(twosum(nums,target))





#sorting and binary search approach
# Function to perform binary search
def binarySearch(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def twoSum(arr, target):
    arr.sort()

    for i in range(len(arr)):
        complement = target - arr[i]

        # Use binary search to find the complement
        if binarySearch(arr, i + 1,
                    len(arr) - 1, complement):
            return True
            
    # If no pair is found
    return False
  	
if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2

    if twoSum(arr, target):
        print("true")
    else:
        print("false")


#using set 


def tWosum(arr,target):


    seen_numbers=set()
    for i in range(len(arr)):
        
        if target-arr[i] in seen_numbers:
            return True
        seen_numbers.add(arr[i])
    return False

if __name__ == "__main__":
    arr = [2,5,3,7,4,1]
    target =8
    if tWosum(arr,target):
        print("true")
    else:
        print("false")
