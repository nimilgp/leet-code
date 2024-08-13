class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = set()
        def backtrack(pattern, usedset):
            if len(pattern) == len(nums):
                ans.append(pattern[:])
                return
            for num in nums:
                if num in usedset:
                    continue
                usedset.add(num)
                pattern.append(num)
                backtrack(pattern, usedset)
                pattern.pop()
                usedset.remove(num)
        backtrack([], used)
        return ans
