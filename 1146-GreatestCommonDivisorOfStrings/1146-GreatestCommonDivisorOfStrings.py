# Last updated: 02/07/2026, 20:20:14
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # check if length of str2 is longer than str1
        if len(str2) > len(str1):
            # if yes, then swap them
            str1, str2 = str2, str1  

        if str2 == str1:
            return str1

        if str1[:len(str2)] != str2:
            return ""

        return self.gcdOfStrings(str1[len(str2):], str2)



        # this problem uses recursion and is about splitting the strings up
        # https://www.youtube.com/watch?v=06oWnxVIAv0