# Last updated: 02/07/2026, 20:20:25
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        # an anagram is a word that can be rearranged to make another word

        # we need a hashmap to count the frequencies of each letter
        # then make sure the two hashmaps are the same for s and t

        dic_s = {} # char:count

        # loop over chars
        for char in s:
            # check if char is in the hashmap
            if char in dic_s:
                # increment the count
                dic_s[char] += 1
            # if char is not in the hashmap
            else:
                # add it to the hashmap and give freq of 1
                dic_s[char] = 1
        
        dic_t = {} # char:count

        # loop over chars
        for char in t:
            # check if char is in the hashmap
            if char in dic_t:
                # increment the count
                dic_t[char] += 1
            # if char is not in the hashmap
            else:
                # add it to the hashmap and give freq of 1
                dic_t[char] = 1
        
        if dic_s == dic_t:
            return True
        return False