class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(coins)
        subsets = []
        
        # Precompute LCM and sign for all non-empty subsets (Inclusion-Exclusion)
        for size in range(1, n + 1):
            sign = 1 if size % 2 == 1 else -1
            for comb in combinations(coins, size):
                lcm_val = comb[0]
                for num in comb[1:]:
                    lcm_val = (lcm_val * num) // gcd(lcm_val, num)
                subsets.append((lcm_val, sign))
                
        def count(x):
            return sum(sign * (x // lcm_val) for lcm_val, sign in subsets)

        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans