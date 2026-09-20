class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i, ch in enumerate(s, 1):
            rev_val = 26 - (ord(ch) - ord('a'))
            total += rev_val * i
        return total