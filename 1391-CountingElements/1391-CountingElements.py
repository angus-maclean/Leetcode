# Last updated: 02/07/2026, 20:20:06
class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        # initialise a counter
        count = 0
        # create a set
        hashset = set()

        # loop through items in the array and add them all to a set
        for i in arr:
            hashset.add(i)
        # loop through each x in the array and see if x+1 is in the set
        for num in arr:
            if num+1 in hashset: 
                # increment the counter
                count += 1
        return count 
