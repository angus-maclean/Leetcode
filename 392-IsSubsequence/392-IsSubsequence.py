# Last updated: 02/07/2026, 20:20:21
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # initialise pointers
        sp, tp = 0, 0
        # while the pointers haven't reached the end
        while sp < len(s) and tp < len(t):
            # if the elements match
            if s[sp] == t[tp]:
                # increment the s pointer along -> only if they match
                sp += 1
            # always increment the t pointer along
            tp += 1
        # return True if the s pointer reaches the end of s string
        return sp == len(s)