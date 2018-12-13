class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 超出时间限制
        # for i in range(len(nums)):
        #     if nums[i] not in nums[i + 1:] and nums[i] not in nums[0:i]:
        #         return nums[i]

        # 标准答案
        a = 0
        for num in nums:
            a ^= num
        return a
    

if __name__ == '__main__':
    nums = [1, 1, 2, 3, 2]
    s = Solution()
    print(s.singleNumber(nums))
