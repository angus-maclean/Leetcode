# Last updated: 02/07/2026, 20:20:08
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        # we are only checking to see if a characteer has been sseen once
        # so we don't need a map, just a set.

        # if a char is already in the set then we return that letter

        # pseudocode

        # make a set
        # loop through the characters
            # check if char is in set
                # if it is then return it
            # if not in set then add it

        a_set = set()

        for char in s:
            if char in a_set:
                return char
            else:
                a_set.add(char)
        return False
