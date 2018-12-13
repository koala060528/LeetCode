# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        lisP = []
        lisQ = []
        self.getStructure(p, lisP)
        self.getStructure(q, lisQ)
        return lisP == lisQ

    def getStructure(self, head, lis):
        if head is None:
            lis.append(head)
            return
        else:
            lis.append(head.val)
        # if head.left is None and head.right is None:
        #     lis.append(head.val)
        #     return head
        # if head.left is not None:
        self.getStructure(head.left, lis)
        # if head.right is not None:
        self.getStructure(head.right, lis)


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.left.left = TreeNode(4)
    head.right = TreeNode(3)
    head.right.left = TreeNode(5)
    head1 = TreeNode(1)
    head1.left = TreeNode(2)
    head1.left.left = TreeNode(4)
    head1.right = TreeNode(3)
    head1.right.left = TreeNode(5)
    lis = []
    lis1 = []
    s = Solution()
    s.getStructure(head, lis)
    s.getStructure(head1, lis1)
    print(lis == lis1)
