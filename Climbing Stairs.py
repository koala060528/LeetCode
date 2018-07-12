class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 这道题就是一个斐波那契序列
        if n == 1:
            return 1
        r = 2
        r_ = 1
        res = 2
        while n > 2:
            res = r + r_
            r_ = r
            r = res
            n -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(4))
