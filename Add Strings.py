class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) > len(num2):
            for i in range(len(num1) - len(num2)):
                num2 = '0' + num2
        else:
            for i in range(len(num2) - len(num1)):
                num1 = '0' + num1

        offset = 0
        res = ''
        tmp = 0
        for i in range(len(num1))[::-1]:
            tmp = int(num1[i]) + int(num2[i]) + offset
            if tmp >= 10:
                res = str(tmp - 10) + res
                offset = 1
            else:
                res = str(tmp) + res
                offset = 0
        if offset == 1:
            res = '1' + res
        return res


if __name__ == '__main__':
    num1 = '436'
    num2 = '564'
    s = Solution()
    print(s.addStrings(num1, num2))
