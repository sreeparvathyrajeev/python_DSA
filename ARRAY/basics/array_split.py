def matrixfn(n,matrix):
    even=[]
    odd=[]
    for i in range(n):
        if matrix[i]%2==0:
            even.append(matrix[i])
        else:
            odd.append(matrix[i])
    even.sort()
    odd.sort()
    return even[-2]+odd[-2]


