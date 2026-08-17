class Solution(object):
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        if n <= 1:
            return 0

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        maxL = [[0] * n for _ in range(n)]
        maxR = [[0] * n for _ in range(n)]

        for i in range(n):
            maxL[i][i] = stoneValue[i]
            maxR[i][i] = stoneValue[i]

        for i in range(n - 1, -1, -1):
            mid = i
            for j in range(i + 1, n):
                total = pref[j + 1] - pref[i]

                while (pref[mid + 1] - pref[i]) * 2 < total:
                    mid += 1

                left_sum_2 = (pref[mid + 1] - pref[i]) * 2
                res = 0

                if left_sum_2 == total:
                    res = (pref[mid + 1] - pref[i]) + max(dp[i][mid], dp[mid + 1][j])
                    if mid > i:
                        res = max(res, maxL[i][mid - 1])
                    if mid + 2 <= j:
                        res = max(res, maxR[mid + 2][j])
                else:
                    if mid > i:
                        res = max(res, maxL[i][mid - 1])
                    if mid + 1 <= j:
                        res = max(res, maxR[mid + 1][j])

                dp[i][j] = res
                maxL[i][j] = max(maxL[i][j - 1], total + res)
                maxR[i][j] = max(maxR[i + 1][j], total + res)

        return dp[0][n - 1]
        