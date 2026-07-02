# Last updated: 02/07/2026, 20:20:23
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # we need to reverse the string in pale
        # that means that we can't use another data structure

        # we can use two pointers, start and end 
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s
