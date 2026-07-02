# Last updated: 02/07/2026, 20:20:15
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        # create a hashmap 
        num_map = {}
        # create array
        num_array = []
        # loop through nums
        for num in nums:
            # check if num is in the hashmap
            if num not in num_map:
                # add the num to the hashmap with count of 1
                num_map[num] = 1
            # else it is in there already so increment the count
            else:
                num_map[num] += 1
        # for the numbers in the dict
        for num in num_map:
            # if the key is 1 ie it has only appeared once
            if num_map[num] == 1:
                # add it to the array
                num_array.append(num)
        # return the largest number in that array else return -1 as the result
        return max(num_array) if num_array else -1

                