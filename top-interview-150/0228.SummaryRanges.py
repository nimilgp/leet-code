class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return ""
        ans = []
        start = nums[0]
        end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(str(start)+"->"+str(end))
                start = nums[i]
                end = nums[i]
            else:
                end = nums[i]
        if start == end:
            ans.append(str(start))
        else:
            ans.append(str(start)+"->"+str(end))
        return ans
