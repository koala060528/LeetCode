class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        if x == 0 or x == 1:
            return x
        r = x
        while r * r > x:
            r = int((r + x / r) / 2)
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(35))
