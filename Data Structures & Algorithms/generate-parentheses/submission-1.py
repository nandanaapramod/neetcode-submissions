class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]

        def back(openb,closedb):
            if openb==closedb==n:
                res.append("".join(stack))
                return
            if openb < n:
                stack.append("(")
                back(openb+1,closedb)
                stack.pop()
            if closedb < openb:
                stack.append(")")
                back(openb,closedb+1)
                stack.pop()
        back(0,0)
        return res
            