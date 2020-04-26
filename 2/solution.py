# Runtime: 68 ms
# Memory Usage: 13.6 MB

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        last = result = ListNode(None)
        up = 0

        while l1 or l2 or up:
            if l1 is not None:
                up += l1.val
                l1 = l1.next
            if l2 is not None:
                up += l2.val
                l2 = l2.next
            last.next = ListNode(up % 10)
            last = last.next
            up //= 10

        return result.next
