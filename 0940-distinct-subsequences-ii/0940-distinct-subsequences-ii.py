class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        end_count = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')
            end_count[idx] = (sum(end_count) + 1) % MOD

        return sum(end_count) % MOD