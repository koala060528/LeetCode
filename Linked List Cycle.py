
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head.next is None:
            return False
        h1 = head
        h2 = head
        while h1.next and h2.next and h2.next.next:
            h1 = h1.next
            h2 = h2.next.next
            if h1 == h2:
                return True

        return False
