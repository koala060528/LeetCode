class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        s = 0
        for i in range(1, len(prices)):
            s = max(s + prices[i] - prices[i - 1], 0)
            res = max(s, res)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
