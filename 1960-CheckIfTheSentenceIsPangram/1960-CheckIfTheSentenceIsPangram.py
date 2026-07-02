# Last updated: 02/07/2026, 20:20:10
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        
        # if we are only looking at one appearance of a letter
        # then a set will do
        
        
        a_set = set()
        
        # loop through the characters
        for letter in sentence:
            a_set.add(letter)
            
        # return True if the set is 26 characters long
        return len(a_set) == 26