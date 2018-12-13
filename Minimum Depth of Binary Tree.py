# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.getDepth(root)
    def getDepth(self,root):
        if root is None:
            return 0
        if root.left is None:
            return self.getDepth(root.right) + 1
        if root.right is None:
            return self.getDepth(root.left) + 1
        l_depth = self.getDepth(root.left) + 1
        r_depth = self.getDepth(root.right) + 1
        if l_depth < r_depth:
            return l_depth
        else:
            return r_depth