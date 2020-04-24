# Runtime: 36 ms
# Memory Usage: 15.1 MB

class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        p = {}
        for i, j in enumerate(nums):
            n = t - j
            if p.__contains__(n):
                return [p[n], i]
            p[j] = i
        return None
