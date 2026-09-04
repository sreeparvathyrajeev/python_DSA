class Solution:
    def reverseWords(self, s):
        lst = s.split()
        rev_lst = lst[::-1]
        new_s = " ".join(rev_lst)
        return new_s