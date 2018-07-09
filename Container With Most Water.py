class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = 0
        left = 0
        right = len(height) - 1
        while left < right:
            m = max(m, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return m


if __name__ == '__main__':
    height = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    s = Solution()
    print(s.maxArea(height))
