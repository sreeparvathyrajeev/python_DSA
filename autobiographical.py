
#O(n^2) time complexity

def autob(s):
    freq={}
    lst=list(map(int,list(s)))
    for i in range(len(lst)):

        freq[i]=lst.count(i)
    
    if list(freq.values())==lst:
        return True
    return False
    

#O(n) time complexity

def autob_efficient(s):
    freq=[0]*len(s)
    for char in s:
        if int(char)>len(s)-1:
            return False
        freq[int(char)]+=1
    for i in range(len(s)):
        if freq[i]!=int(s[i]):
            return False
    
    return len(set(s))
