class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        countL = 0
        countR = 0
        
        def isVowel(char):
            x = char.lower()
            if x == 'a' or x == 'e' or x == 'i' or x == 'u' or x == 'o':
                return True
            return False
        
        while l < r:
            if isVowel(s[l]):
                countL += 1
            if isVowel(s[r]):
                countR += 1
            l += 1
            r -= 1
        
        return countL == countR