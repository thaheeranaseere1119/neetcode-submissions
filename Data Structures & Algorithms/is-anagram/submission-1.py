class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        se={}
        if(len(s)!=len(t)):
            return False
        for char in s:
            if char in se:
                se[char]+=1
            else:
                se[char]=1
        for char in t:
            if char not in se:
                return False
            se[char]-=1
            if se[char]<0:
                return False
        return True

        
        