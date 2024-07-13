class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        hashset = set(nums)
        maxlen = 0
        for element in hashset:
            if (element-1) not in hashset:
                length = 1
                while element+length in hashset:
                    length += 1
                maxlen = max(maxlen, length)
        return maxlen
