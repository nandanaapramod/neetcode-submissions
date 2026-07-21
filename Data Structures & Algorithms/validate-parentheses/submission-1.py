class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brack={")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in brack:
                if stack and stack[-1]==brack[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False
