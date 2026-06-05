# Given an array of integers, find the sum of the second largest even number and the second largest odd number in the array. 
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


