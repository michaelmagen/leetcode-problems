class Solution:
    def reverseWords(self, s: str) -> str:
        # split the string into words
        words = s.split()
        l, r = 0, len(words) - 1
        
        # iterate thorugh words and swap l and r while moving to middle of words
        while l < r:
            temp = words[l] 
            words[l] = words[r]
            words[r] = temp
            l += 1
            r -= 1
        
        # return joined word string
        return ' '.join(words)

    