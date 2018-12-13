class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = s.split()
        if len(ss) == 0:
            return 0
        return len(ss[-1])