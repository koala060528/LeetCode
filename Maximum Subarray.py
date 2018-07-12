import sys


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        m = - sys.maxsize
        for each in nums:
            s += each
            m = max(s, m)
            s = max(s, 0)

        return m
        # for l in range(1, len(nums) + 1):
        #     left = 0
        #     right = l
        #
        #     while right <= len(nums):
        #         if sum(nums[left:right]) > s:
        #             s = sum(nums[left:right])
        #         right += 1
        #         left += 1
        # return s


if __name__ == '__main__':
    s = Solution()
    # print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(s.maxSubArray([-2, -3, -1]))
