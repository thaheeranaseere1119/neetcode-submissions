class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            if n not in seen:
                seen.add(n)
            else:
                return False
            num=0
            while n>0:
                digit=n%10
                num+=digit*digit
                n=n//10
            n=num
        return True

        