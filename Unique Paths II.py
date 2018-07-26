class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = [[0 for i in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = 1
            else:
                break
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                break
        for i in range(1, len(obstacleGrid[0])):
            for j in range(1, len(obstacleGrid)):
                if obstacleGrid[j][i] != 1:
                    dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
                else:
                    dp[j][i] = 0

        return dp[-1][-1]


if __name__ == '__main__':
    obstacleGrid = [[0,0],[1,1],[0,0]]
    s = Solution()
    print(s.uniquePathsWithObstacles(obstacleGrid))
