class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {')': '(', ']':'[', '}':'{'}
        stack = []
        
        for i in s:
            if i not in parMap:
                stack.append(i)
                continue
            if not stack or stack[-1] != parMap[i]:
                return False
            stack.pop()

        return not stack
                