# Last updated: 02/07/2026, 20:20:12
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # create a dict to count specific letters
        count_dict = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}

        # loop through chars in text
        for char in text:
            # if the char is in the dict ie already b-a-l-o-n
            if char in count_dict:
                # incremenet its count
                count_dict[char] += 1

        # get the minimum of number of instances of each letter for the word 'balloon'
        balloon_count = min(
            count_dict["b"],
            count_dict["a"],
            count_dict["l"] // 2,
            count_dict["o"] // 2,
            count_dict["n"],
        )
        # return it
        return balloon_count
