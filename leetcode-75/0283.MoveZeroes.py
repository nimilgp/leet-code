class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroptr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zeroptr] = nums[zeroptr], nums[i]
                zeroptr += 1
