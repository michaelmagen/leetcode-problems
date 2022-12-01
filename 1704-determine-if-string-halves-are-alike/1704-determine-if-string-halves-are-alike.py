class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = s[0:len(s) // 2]
        r = s[len(s) // 2: len(s)]
        countL = 0
        countR = 0
        
        for i in range(len(l)):
            if l[i].lower() == 'a' or l[i].lower() == 'e' or l[i].lower() == 'i' or l[i].lower() == 'u' or l[i].lower() == 'o':
                countL += 1
            if r[i].lower() == 'a' or r[i].lower() == 'e' or r[i].lower() == 'i' or r[i].lower() == 'u' or r[i].lower() == 'o':
                countR += 1
        
        return countL == countR