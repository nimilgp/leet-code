class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        leftp = 0
        sumvar = 0
        count = 1000000 
        for rightp in range(len(nums)):
            sumvar += nums[rightp]
            while leftp<=rightp and sumvar >= target:
                count = min(count, rightp - leftp + 1)
                sumvar -= nums[leftp]
                leftp += 1
        return count if count < 1000000 else 0
