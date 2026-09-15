class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            
            if i >= k:
                sub1 = s[i - k:i]
                if sub1 == sub1[::-1]:
                    dp[i] = max(dp[i], dp[i - k] + 1)
            
            if i >= k + 1:
                sub2 = s[i - k - 1:i]
                if sub2 == sub2[::-1]:
                    dp[i] = max(dp[i], dp[i - k - 1] + 1)
                    
        return dp[n]