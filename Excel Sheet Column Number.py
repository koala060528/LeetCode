class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for index in range(len(s))[::-1]:
            res += pow(26, len(s) - index - 1) * (ord(s[index]) - 64)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber('ZY'))
