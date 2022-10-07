class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {')': '(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            if i in parMap: 
                if len(stack) > 0 and stack[-1] == parMap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack
               
                