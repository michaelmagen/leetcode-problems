class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {} # sorted anagram -> array of anagrams

        for n in strs:
            anag = ''.join(sorted(n))
            if anag in hashMap:
                hashMap[anag].append(n)
            else:
                hashMap[anag] = [n]
        
        answer = []
        for key in hashMap:
            answer.append(hashMap[key])
            
        return answer