# Runtime: 36 ms
# Memory Usage: 15.1 MB

class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        p = {}
        for i, j in enumerate(nums):
            n = t - j
            if p.__contains__(n): # https://stackoverflow.com/a/52885215/8144980
                return [p[n], i]
            p[v] = i
        return None
