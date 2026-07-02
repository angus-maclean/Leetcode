# Last updated: 02/07/2026, 20:20:24
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
            
        # make a set of 0 to n ... a set that isn't missing any numbers
        full_set = set(range(len(nums)+1))
        
        # turns nums list into a set
        nums_set = set(nums)
        
        # get the difference between the sets
        diff_set = full_set.difference(nums_set)
        
        return diff_set.pop()
        
        