# Last updated: 02/07/2026, 20:20:34
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # set two pointers
        l, r = 0, len(nums) - 1

        # while the pointers haven't met
        while l <= r:
            # calculate middle index of search space
            mid = (l + r) // 2
            # compare middle with target
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        # target is not in the array but l is where it would be inserted
        return l