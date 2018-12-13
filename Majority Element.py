class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        middle = int(len(nums) / 2)
        return nums[middle]


if __name__ == '__main__':
    nums = [3, 2, 3, 3, 4]
    s = Solution()
    print(s.majorityElement(nums))
