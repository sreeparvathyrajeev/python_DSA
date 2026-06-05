def max_xor_sum(N,A,k):
    max_xor_sum=0
    for x in range(0,k+1):
        xor_sum=0
        for num in A:
            xor_sum+=x^num
        if xor_sum>max_xor_sum:
            max_xor_sum=xor_sum
    return max_xor_sum
if __name__=="__main__":
    lst=list(map(int,input().split()))
    N=lst[0]
    k=lst[1]
    A=lst[2:]
    answer=max_xor_sum(N,A,k)
    print(answer)
    
