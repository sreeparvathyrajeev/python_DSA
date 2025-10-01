
def recursivefn(count):
    if count>=5:
        return 
    else:
        count+=1
        print("count is:",count)
        recursivefn(count)
def main1():
    count=0
    print("recursion started")
    recursivefn(count)
    print("recursion ended")   

def printnamentimes(n):
    if n<=0:
        return
    else:
        print("pyar")
        n-=1
        printnamentimes(n)
def main2():
    n=int(input("enter number of times"))
    printnamentimes(n)

def print1ton(i,n):
    if i>n:
        return
    else:
        print(i)
        i+=1
        print1ton(i,n)
def main3():
    n=int(input("enter a number"))
    i=1
    print1ton(i,n)

def printnto1(n):
    if n==0:
        return
    else:
        print(n)
        n-=1
        printnto1(n)
def main4():
    n=int(input("enter a number"))
    printnto1(n)

def backtrack(n):
    if n<=0:
        return
    else:
        backtrack(n-1)
        print(n)
def main5():
    n=int(input("enter a number"))
    backtrack(n)


