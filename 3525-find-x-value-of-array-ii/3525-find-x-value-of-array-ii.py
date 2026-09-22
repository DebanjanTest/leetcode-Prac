class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        tree_size = 1
        while tree_size < n:
            tree_size *= 2

        # count[node][rem] = number of prefixes in node's segment with product % k == rem
        count = [[0] * k for _ in range(2 * tree_size)]
        prod = [1] * (2 * tree_size)

        def build(idx, l, r):
            if l == r:
                if l < n:
                    val = nums[l] % k
                    prod[idx] = val
                    count[idx][val] = 1
                return
            mid = (l + r) // 2
            build(2 * idx, l, mid)
            build(2 * idx + 1, mid + 1, r)
            p_left = prod[2 * idx]
            prod[idx] = (p_left * prod[2 * idx + 1]) % k
            for rem in range(k):
                count[idx][rem] = count[2 * idx][rem] + count[2 * idx + 1][(rem * pow(p_left, -1, k) if False else 0)]  # structure placeholder

        # Direct merge
        def pull(idx):
            left = 2 * idx
            right = 2 * idx + 1
            p_left = prod[left]
            prod[idx] = (p_left * prod[right]) % k
            for rem in range(k):
                count[idx][rem] = count[left][rem]
            for rem in range(k):
                count[idx][(p_left * rem) % k] += count[right][rem]

        for i in range(n):
            idx = tree_size + i
            val = nums[i] % k
            prod[idx] = val
            count[idx][val] = 1

        for i in range(tree_size - 1, 0, -1):
            pull(i)

        def update(pos, val):
            idx = tree_size + pos
            val %= k
            prod[idx] = val
            count[idx] = [0] * k
            count[idx][val] = 1
            idx //= 2
            while idx > 0:
                pull(idx)
                idx //= 2

        # Query range [ql, qr]
        def query(idx, l, r, ql, qr, cur_prod, cur_counts):
            if ql <= l and r <= qr:
                for rem in range(k):
                    cur_counts[(cur_prod * rem) % k] += count[idx][rem]
                cur_prod = (cur_prod * prod[idx]) % k
                return cur_prod
            mid = (l + r) // 2
            if ql <= mid:
                cur_prod = query(2 * idx, l, mid, ql, qr, cur_prod, cur_counts)
            if qr > mid:
                cur_prod = query(2 * idx + 1, mid + 1, r, ql, qr, cur_prod, cur_counts)
            return cur_prod

        ans = []
        for index_i, value_i, start_i, x_i in queries:
            update(index_i, value_i)
            cur_counts = [0] * k
            query(1, 0, tree_size - 1, start_i, n - 1, 1, cur_counts)
            ans.append(cur_counts[x_i])

        return ans