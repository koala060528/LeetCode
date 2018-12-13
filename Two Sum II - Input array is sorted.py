class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for i in range(len(numbers)):
            rest = target - numbers[i]
            if rest in dic.keys():
                return dic[rest] + 1, i + 1
            else:
                dic[numbers[i]] = i


if __name__ == '__main__':
    s = Solution()
    numbers = [2, 7, 7, 7, 7, 7, 11, 15]
    target = 13
    print(s.twoSum(numbers, target))
