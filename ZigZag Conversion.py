class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        lis = list()
        for i in range(numRows):
            lis.append(list())

        i = 0
        j = 0
        try:
            while True:
                remainder = j % (numRows - 1)
                j += 1
                if remainder == 0:
                    for each in lis:
                        each.append(s[i])
                        i += 1
                else:
                    for each in lis:
                        each.append(None)
                    lis[-(remainder + 1)][-1] = s[i]
                    i += 1
        except:
            pass
        res = ''
        for l in lis:
            for word in l:
                if word:
                    res += word
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.convert('PAYPALISHIRING', 1))
