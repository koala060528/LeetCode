class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = 0
        res = ''
        for i in range(0, len(digits))[::-1]:
            if i == len(digits) - 1:
                tmp = digits[i] + 1 + flag
            else:
                tmp = digits[i] + flag
            if tmp >= 10:
                res = str(tmp - 10) + res
                flag = 1
            else:
                res = str(tmp) + res
                flag = 0
        if flag == 1:
            res = '1' + res
        resDigits = []
        for i in res:
            resDigits.append(int(i))

        return resDigits


if __name__ == '__main__':
    digits = [9, 9, 9]
    s = Solution()
    res = s.plusOne(digits)
    print(res)
