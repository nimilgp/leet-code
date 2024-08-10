class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexMap = {}
        for i in range(len(nums)):
            if nums[i] not in indexMap:
                indexMap[nums[i]] = i
            else:
                if abs(indexMap[nums[i]] - i) <= k:
                    return True
                else:
                    indexMap[nums[i]] = i
        return False
