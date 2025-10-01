def evenodd(A):
    N=len(A)
    result =""
    for i in range (N):
        if A[i]%2==0:
            result +="Even"
        else:
            result +="Odd"
    return result
if __name__ =="__main__":
    A=list(map(int,input().split()))
    print(evenodd(A))
