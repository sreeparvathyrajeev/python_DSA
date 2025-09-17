class Solution:
    def groupAnagrams(self, strs):
        group_anagrams=[]
        for j in range(len(strs)):
            if strs[j]!="PASS":
                group_anagrams_element=[strs[j]]
                for k in range(1,len(strs)-j):
                    if self.isAnagram(strs[j],strs[j+k]) and strs[j+k]!="PASS":
                        group_anagrams_element.append(strs[j+k])
                        strs[j+k]="PASS"
                    
                group_anagrams.append(group_anagrams_element)
        return group_anagrams


    def isAnagram(self, s: str, t: str) -> bool:
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
    
    def __init__(self):
        pass

obj=Solution()
strs=["car"]
print(obj.groupAnagrams(strs))