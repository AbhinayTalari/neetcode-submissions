class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if i in d:
                stack.append(i)
            elif not stack or d[stack.pop()] != i:
                return False
        return len(stack) == 0