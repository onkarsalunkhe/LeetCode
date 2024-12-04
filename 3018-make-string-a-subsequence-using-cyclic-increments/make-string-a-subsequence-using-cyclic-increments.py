class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i,j=0,0
        flag = False
        while i<len(str1) and j<len(str2):
            val = (ord(str1[i])+1-ord(str2[j]))%26
            if val==0 or val==1:
                i+=1
                j+=1
                flag = True
            else:
                i+=1
                flag = False
        
        if j<len(str2):
            return False
        return flag
