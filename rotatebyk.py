#brute

def rotatebykclk(arr,k):
    n=len(arr)
    for i in range(k):
        temp=arr[n-1]
        for j in range(n-1):
            arr[n-j-1]=arr[n-j-2]
        arr[0]=temp
    return arr


#optimal

def rotate(arr,k):
    n=len(arr)
    k=k%n
    return arr[-k:]+arr[:-k]





if __name__ =="__main__":
    elements=str(input()).split()
    arr=[int(i) for i in elements]
    k=int(input())
    
    print(rotate(arr,k))


