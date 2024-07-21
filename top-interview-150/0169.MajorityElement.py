class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        minsize = len(nums)//2
        if minsize == 0:
            return nums[0]
        d = {}
        for e in nums:
            if e not in d:
                d[e] = 1
            else:
                d[e] += 1
                if d[e] > minsize:
                    return e

