# Runtime: 44 ms
# Memory Usage: 15.2 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in p:
                p[num] = i
            else:
                return [p[n], i]
