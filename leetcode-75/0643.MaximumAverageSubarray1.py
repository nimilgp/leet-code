class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tot = window = sum(nums[:k])
        for i in range(k, len(nums)):
            window += nums[i] - nums[i-k]
            tot = max(tot, window)
        return tot/k
