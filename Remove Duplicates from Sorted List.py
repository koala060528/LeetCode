class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        cur = head
        next = head.next

        while(next is not None):
            if cur.val == next.val:
                next = next.next
                if next is None:
                    cur.next = None
            else:
                cur.next = next
                cur = cur.next
                next = next.next

        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)

    s = Solution()
    res = s.deleteDuplicates(head)
    pass
