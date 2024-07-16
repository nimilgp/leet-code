class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(arr, x, low, high):
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] == x:
                    return mid
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[l] > nums[mid]: # check for inflection point in left half
                if target >= nums[mid] and target <= nums[r]: # check if target in right part
                    l = mid
                    return binarySearch(nums, target, l, r)
                else:
                    r = mid - 1
            else: # inflection point is on right
                if target <= nums[mid] and target >= nums[l]:
                    r = mid
                    return binarySearch(nums, target, l, r)
                else:
                    l = mid + 1
        return -1 
