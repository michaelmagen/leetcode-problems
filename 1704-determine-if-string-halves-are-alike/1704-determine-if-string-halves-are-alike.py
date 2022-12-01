class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = s[0:len(s) // 2]
        r = s[len(s) // 2: len(s)]
        countL = 0
        countR = 0
        
        def isVowel(char):
            x = char.lower()
            if x == 'a' or x == 'e' or x == 'i' or x == 'u' or x == 'o':
                return True
            return False
        
        for i in range(len(l)):
            if isVowel(l[i]):
                countL += 1
            if isVowel(r[i]):
                countR += 1
        
        return countL == countR