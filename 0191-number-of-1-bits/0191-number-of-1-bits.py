class Solution:
    def hammingWeight(self, n: int) -> int:
        # mod 2 tells us if there is one at last bit place, >> shifts the bits right
        res = 0
        while n != 0:
            res += n % 2
            n = n >> 1
        return res