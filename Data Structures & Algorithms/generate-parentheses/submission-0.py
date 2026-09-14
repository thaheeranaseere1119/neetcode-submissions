class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def back(openn,closed):
            if openn==closed==n:
                res.append("".join(stack))
                return 
            if openn<n:
                stack.append("(")
                back(openn+1,closed)
                stack.pop()
            if closed<openn:
                stack.append(")")
                back(openn,closed+1)
                stack.pop()
        back(0,0)
        return res

        