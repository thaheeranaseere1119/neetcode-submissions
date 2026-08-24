class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        left=0
        sett=set()
        for i in range(len(s)):
            while s[i] in sett:
                sett.remove(s[left])
                left+=1
                
            else:
                sett.add(s[i])
            max_len=max(max_len,len(sett))
        return max_len
            
            



        