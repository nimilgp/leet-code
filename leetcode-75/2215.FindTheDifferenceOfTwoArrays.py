class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = set(nums1)
        ans2 = set(nums2)
        answer1 = []
        answer2 = []
        for num in ans1:
            if num not in ans2:
                answer1.append(num)
        for num in ans2:
            if num not in ans1:
                answer2.append(num)
        return [answer1,answer2]

