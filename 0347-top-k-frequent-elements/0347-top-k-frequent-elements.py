class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # value -> count
        freq = [[] for i in range(len(nums) + 1)] # create len(nums) empty arrays

        for n in nums:
            # get the count
            count[n] = 1 + count.get(n, 0) # default value of 0 
        for n, c in count.items():
            # copy the frequency info to array
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            # add the last k elements from freq to res
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            

            