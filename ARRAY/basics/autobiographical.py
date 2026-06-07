# An autobiographical number is a number N such that the first digit of N counts how many 0s are in N, the second digit counts how many 1s are in N, and so on.

#O(n^2) time complexity because the count function is O(n) and we are calling it n times.

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
    
    return True
