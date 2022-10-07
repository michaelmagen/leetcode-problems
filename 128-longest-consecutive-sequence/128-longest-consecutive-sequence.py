class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Set = set(nums)
        longest = 0
        #iterate through nums
        for n in nums:
            # if num is start of sequence check sequence length
            # n is start of sequence if n - 1 not in set
            if (n - 1) not in Set:
                length = 0
                while (n + length) in Set:
                    length += 1
                longest = max(length, longest)
        return longest