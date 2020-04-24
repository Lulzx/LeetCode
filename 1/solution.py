# Runtime: 5920 ms
# Memory Usage: 14.8 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = len(nums)
        for i in range(p):
            n = i + 1
            for j in range(n, p):
                if nums[i] + nums[j] == target:
                    return [i, j]
