# Last updated: 02/07/2026, 20:20:35
class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "}": "{", "]": "["}
        stack = []
        for bracket in s:
            # if CLOSING bracket is in hashmap - the keys are closing brackets
            if bracket in hashmap:
                # if the stack is not empty and the last element of the stack matches
                if stack and stack[-1] == hashmap[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        # return True if the stack is empty otherwise return False
        return True if not stack else False
    