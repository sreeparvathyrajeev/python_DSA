import math

def beautysum(n,tree,parent):
    #creating a dictionary to store children of each node
    children_dict={}
    for i in range(1,n+1):
        children_dict[i]=[]
    for i in range(1,n+1):
        p=parent[i-1]
        if p!=0:
            children_dict[p].append(i)
    #function to calculate beauty of each subtree
    def beauty(node):
        result=0
        child1=children_dict[node][0] if len(children_dict[node])>0 else None
        child2=children_dict[node][1] if len(children_dict[node])>1 else None
        if child1 is not None:
            if math.sqrt(tree[child1-1]*tree[node-1])%1==0:
                result+=1
        if child2 is not None:
            if math.sqrt(tree[child2-1]*tree[node-1])%1==0:
                result+=1   
        if child1 is not None and child2 is not None:

            if math.sqrt(tree[child1-1]*tree[child2-1])%1==0:
                result+=1
        
        return result
    total_beauty=0
    i=n
    beautyarray=[0]*n
    while i>=1:
        if len(children_dict[i])>0:
            beautyarray[i-1]=beauty(i)+beautyarray[children_dict[i][0]-1] 
        else:
            beautyarray[i-1]=beauty(i)
        if len(children_dict[i])>1 :
            beautyarray[i-1]=beautyarray[i-1]+beautyarray[children_dict[i][1]-1] 
        

        
        total_beauty+=beautyarray[i-1]
        
        i-=1
    return total_beauty


if __name__=="__main__":
    a=list(map(int,input().split()))
    parent=[]
    tree=[]
    n=a[0]
    for i in range(1,n+1):
        parent.append(a[i])
    for i in range(n+1,len(a)):
        tree.append(a[i])
    sum=beautysum(n,tree,parent)
    result=sum%(10**9+7)
    print(result)
    