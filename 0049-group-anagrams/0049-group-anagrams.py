class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # put every anagram in hashmap
        answer = collections.defaultdict(list) # letters present -> array of anagrams
        
        for s in strs:
            # array for each letter in alpahbet, keeps track of count of letters
            count = [0] * 26
            for c in s:
                # get letter using ascii value
                count[ord(c) - ord("a")] += 1
            answer[tuple(count)].append(s) # need tuple bc map key cant be list
        return answer.values()