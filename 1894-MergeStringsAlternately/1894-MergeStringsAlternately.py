# Last updated: 02/07/2026, 20:20:04
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # add word1 letter, then word2 letter, then word1 letter, etc...
        # we are adding from two different lists so use two pointers


        merged = [] # make a new list that we can append to
        p1, p2 = 0, 0 # a pointer for each word

        while p1 < len(word1) and p2 < len(word2): # while pointers haven't reached the end
                merged.append(word1[p1]) # add word1 letter
                p1 += 1 # move p1 along
                merged.append(word2[p2]) # add word2 letter
                p2 += 1 # move p2 along
        if p1 < len(word1): 
            merged.extend(word1[p1:]) # add the remaining elements to the merged list
        elif p2 < len(word2):
            merged.extend(word2[p2:])

        # convert the merged list into a string
        return "".join(merged)



