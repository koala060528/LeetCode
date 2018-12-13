# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.judge(root.left, root.right)

    def judge(self, left, right):
        if (left is None and right is not None) or (left is not None and right is None):
            return False
        if left is not None and right is not None:
            if left.val != right.val:
                return False
            else:
                return self.judge(left.left, right.right) and self.judge(left.right, right.left)
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    # root.right.left = TreeNode(4)
    root.left = TreeNode(2)
    # root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    print(s.isSymmetric(root))
