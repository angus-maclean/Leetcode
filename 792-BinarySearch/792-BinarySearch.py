# Last updated: 02/07/2026, 20:20:19
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # declare the search space with two pointers
        l = 0
        r = len(nums) - 1

        # while the l index hasn't met the r index
        while l <= r:
            # calculate the middle index of the search space
            mid = (l + r) // 2
            # compare number at index mid to target number
            if nums[mid] == target:
                return mid
            # if number at index mid is greater than target
            elif nums[mid] > target:
                r = mid - 1
            # number at index mid is less than target
            elif nums[mid] < target:
                l = mid + 1
        return - 1

