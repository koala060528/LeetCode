# class NumArray:
#
#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.nums = nums
#
#     def sumRange(self, i, j):
#         """
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         nums = self.nums[i:j+1]
#         return sum(nums)


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        dp = list()
        dp.append(0)
        for i in range(len(nums)):
            dp.append(sum(nums[0:i + 1]))
        self.dp = dp

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j + 1] - self.dp[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    print(obj.sumRange(2, 5))
