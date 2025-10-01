def pattern1(n):
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
        print("\n")
def pattern2(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print("\n")
def pattern3(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print("*",end="")
        print("\n")
def pattern4(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(j+1,end="")
        print("\n")
def pattern5(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print(j+1,end="")
        print("\n")
def pattern6(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(i+1,end="")
        print("\n")
def pattern7(n):
    for i in range(0,n):
        for j in range(0,(((2*n)-1)-((2*i)+1))//2):
            print(" ",end="")
        for k in range(0,2*i+1):
            print("*",end="")
        for m in range(0,(((2*n)-1)-((2*i)+1))//2):
            print(" ",end="")
        print("\n")
def pattern8(n):
    for i in range(0,n):
        for j in range(0,(((2*n)-1)-((2*i)+1))//2):
            print(" ",end="")
        for k in range(0,2*i+1):
            print(k+1,end="")
        for m in range(0,(((2*n)-1)-((2*i)+1))//2):
            print(" ",end="")
        print("\n")




rows=input("enter number of rows")
print(pattern7(int(rows)))
