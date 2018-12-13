class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lis = list()
        for each in s:
            if ord(each) >= 48 and ord(each) <= 57:
                lis.append(each)
            elif ord(each) >= 65 and ord(each) <= 90:
                lis.append(each)
            elif ord(each) >= 97 and ord(each) <= 122:
                lis.append(each.upper())
        l = 0
        r = len(lis) - 1
        while(l<r):
            if lis[l] != lis[r]:
                return False
            l += 1
            r -= 1
        return True

if __name__ == '__main__':
    str = 'A man, a plan, a canal: Panama'
    s = Solution()
    print(s.isPalindrome(str))
