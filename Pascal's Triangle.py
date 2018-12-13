class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = []
        res.append([1])
        for i in range(1, numRows):
            temp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(temp)
        return res


if __name__ == '__main__':
    s = Solution()
    for l in s.generate(5):
        print(l)
