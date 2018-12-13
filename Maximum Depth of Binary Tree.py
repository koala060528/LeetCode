# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return (left if left > right else right) + 1

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    # root.right.left = TreeNode(4)
    root.left = TreeNode(2)
    # root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    print(s.maxDepth(root))
