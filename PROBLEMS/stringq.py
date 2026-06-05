num = list(map(int,list(str(input()))))
dig = int(str(input()))
pos=[]
for i in range(len(num)):
    if num[i]==dig:
        pos.append(i)
max=0
for j in range(len(pos)):
    num2=num.copy()
    del num2[pos[j]]
    s="".join(map(str,num2))
    if int(s)>max:
        max=int(s)
print(max)
    
