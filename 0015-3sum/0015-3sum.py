class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # allows us to skip over duplicates

        for i, a in enumerate(nums):
            # skip over duplicates
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1 # two-pointer
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1 # move pointer to get smaller value
                elif threeSum < 0:
                    l += 1 # move pointer to get larger value
                else:
                    res.append([a, nums[l], nums[r]]) # sum found
                    # update left pointer to the next non duplicate num
                    l += 1  
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res