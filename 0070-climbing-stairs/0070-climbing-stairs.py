class Solution:
    def climbStairs(self, n: int) -> int:
        # like fibonacci. to get number of paths n, take (n - 1) + (n - 2)
        one, two = 1, 1
        
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
            
        return one 