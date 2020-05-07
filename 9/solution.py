# Runtime: 52 ms
# Memory Usage: 14 MB

class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        if x >= 0 and n == n[::-1]:
            return True
        else:
            return False
