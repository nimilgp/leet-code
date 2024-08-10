class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        tmp = nums[-1*k:]
        nums[k:] = nums[:-1*k]
        nums[:k] = tmp[:]
