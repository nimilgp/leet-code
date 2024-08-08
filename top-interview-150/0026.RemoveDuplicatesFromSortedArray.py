class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq = set()
        index = 0
        for i in range(len(nums)):
            num = nums[i]
            if num not in uniq:
                uniq.add(num)
                nums[index] = num
                index += 1
        return len(uniq)
