class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create arrray size len(nums) with 1 at each position
        res = [1] * len(nums) 
        
        prefix = 1 # prodict of nums before current one
        # calculate prefix of each num and store in res
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] 
        
        postfix = 1
        # calculate postfix of each num and multiply it by prefix then store in res
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        