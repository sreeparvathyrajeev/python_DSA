def isAnagram(s: str, t: str) -> bool:
        lst_s=list(s)
        lst_t=list(t)
        
        n=len(lst_t)
        m=len(lst_s)
        
        s_freq={}

        for letter in lst_s:
            s_freq[letter]=s_freq.get(letter,0)+1


        if n!=m:
            return False

        for i in range(n):
            if lst_t[i] not in s_freq:
                return False

            elif s_freq[lst_t[i]]!=0:
                s_freq[lst_t[i]]-=1
                
            else:
                return False
        return True

if __name__ =="__main__":
    s=input()
    t=input()
    print(isAnagram(s,t))
