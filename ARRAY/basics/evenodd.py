# Given an array of integers, return a string where each integer is replaced by "Even" if it is even and "Odd" if it is odd.
# Use "Even" for even numbers and "Odd" for odd numbers.
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
