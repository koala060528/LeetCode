# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.order(root, 0, res)
        lis = []
        for i in range(0,len(res))[::-1]:
            lis.append(res[i])
        return lis

    def order(self, root, depth, res):
        if root is None:
            return
        if len(res) == depth:
            res.append(list())
        res[depth].append(root.val)
        if root.left is not None:
            self.order(root.left, depth + 1, res)
        if root.right is not None:
            self.order(root.right, depth + 1, res)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    # root.right.left = TreeNode(4)
    root.left = TreeNode(2)
    # root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    print(s.levelOrderBottom(root))
