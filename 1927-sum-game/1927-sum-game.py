class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        mid = len(num) // 2

        s1 = sum(int(c) for c in num[:mid] if c != "?")
        s2 = sum(int(c) for c in num[mid:] if c != "?")

        q1 = num[:mid].count("?")
        q2 = num[mid:].count("?")

        return (s1 - s2) != (q2 - q1) * 4.5