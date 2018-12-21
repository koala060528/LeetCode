class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 暴力方法，会超出时间限制
        # res = 1
        # while n > 0:
        #     res *= n
        #     n -= 1
        # print(res)
        # num = 0
        # for i in range(len(str(res)))[::-1]:
        #     if str(res)[i] == "0":
        #         num += 1
        #     else:
        #         break
        # return num

        # 方法二：若一个数能被5的N次方整除，则+n
        # res = 0
        # index = 5
        #
        # while index <= n:
        #     if index == 120:
        #         i = 120
        #     temp = index
        #     while temp >= 5:
        #         if temp % 5 == 0:
        #             res += 1
        #             temp = int(temp / 5)
        #         else:
        #             break
        #     index += 5
        # return res

        # 方法三：
        total = 0
        while n >= 1:
            n //= 5
            total += n
        return total


if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeroes(130))
