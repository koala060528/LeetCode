class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a is None:
            return b
        if b is None:
            return a
        flag = 0
        res = ''
        if len(a) > len(b):
            for i in range(0, len(a) - len(b)):
                b = '0' + b
        else:
            for i in range(0, len(b) - len(a)):
                a = '0' + a
        for i in range(0, len(a))[::-1]:
            aa = a[i]
            bb = b[i]
            tmp = int(aa) + int(bb) + flag
            if tmp == 2:
                res = '0' + res
                flag = 1
            elif tmp == 3:  # 这题的坑就在这里，进位可能大于1
                res = '1' + res
            else:
                res = str(tmp) + res
                flag = 0
        if flag == 1:
            res = '1' + res

        return res


if __name__ == '__main__':
    s = Solution()
    a = "1111"
    b = "1111"
    print(s.addBinary(a, b))
