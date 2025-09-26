def rotate(matrix1):
    n = len(matrix1)
    m = len(matrix1[0])

    matrix2 = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrix2[j][n-1-i] = matrix1[i][j]
    return matrix2
if __name__ == "__main__":
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    print(rotate(matrix1))