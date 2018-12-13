class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        lis = list()
        while n > 0:
            remainder = n % 26
            if remainder == 0:
                lis.append(26)
                n -= 1
            else:
                lis.append(remainder)
            n = int(n / 26)
        res = ''
        lis.reverse()
        for num in lis:
            res += chr(num + 64)
        return res


if __name__ == '__main__':
    n = 703
    s = Solution()
    print(s.convertToTitle(n))
