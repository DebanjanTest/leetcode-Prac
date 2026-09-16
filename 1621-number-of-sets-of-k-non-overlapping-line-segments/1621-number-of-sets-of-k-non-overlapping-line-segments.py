class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        total_n = n + k - 1
        total_r = 2 * k

        if total_r > total_n:
            return 0

        total_r = min(total_r, total_n - total_r)

        numerator = 1
        denominator = 1

        for i in range(total_r):
            numerator = (numerator * (total_n - i))
            denominator = (denominator * (i + 1))

        ans = (numerator // denominator) % MOD
        return ans