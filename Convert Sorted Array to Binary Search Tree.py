# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        res = self.sort(nums,  0, len(nums) - 1)
        return res

    def sort(self, nums, left, right):
        if left > right:
            return
        cur = TreeNode(nums[int((right+left)/2)])

        cur.left = self.sort(nums,  left, int((right + left) / 2) - 1)
        cur.right= self.sort(nums,  int((right + left) / 2) + 1, right)
        return cur


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    s = Solution()
    print(s.sortedArrayToBST(nums))
