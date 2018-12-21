class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 超出时间限制
        # for each in range(k):
        #     for i in range(1, len(nums))[::-1]:
        #         tmp = nums[i]
        #         nums[i] = nums[i - 1]
        #         nums[i - 1] = tmp
        # return nums
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, left, right):
        while left < right:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1
            right -= 1


if __name__ == '__main__':
    nums = [1, 2]
    k = 3
    s = Solution()
    s.rotate(nums, k)
    print(nums)
