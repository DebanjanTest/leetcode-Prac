class Solution(object):
    def countCommas(self, n):
        p=1000
        res=0

        while p<=n:
            res+=n-p+1
            p*=1000

        return res

        """
        :type n: int
        :rtype: int
        """
        