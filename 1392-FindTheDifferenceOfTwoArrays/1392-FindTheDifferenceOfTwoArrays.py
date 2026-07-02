# Last updated: 02/07/2026, 20:20:07
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        difference1 = set1 - set2
        difference2 = set2 - set1
        list1 = list(difference1)
        list2 = list(difference2)
        return list1, list2


        