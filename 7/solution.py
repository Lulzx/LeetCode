# Runtime: 32 ms
# Memory Usage: 13.8 MB

class Solution:
    def reverse(self, x: int) -> int:
        rev = str(x)[::-1]
        if rev[-1:] is not '-':
            x = int(rev)
        else:
            x = -1 * int(rev[:-1])
        if x < -2147483648 or x > 2147483647:
            return 0
        return x
