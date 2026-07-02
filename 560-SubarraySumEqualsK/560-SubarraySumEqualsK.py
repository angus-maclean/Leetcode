# Last updated: 02/07/2026, 20:20:20
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev_sum = Counter({0:1})
        n, prefix_sum, res = len(nums), 0, 0

        for i in range(n):
            prefix_sum += nums[i]

            res += prev_sum[prefix_sum - k]

            prev_sum[prefix_sum] += 1
        
        return res