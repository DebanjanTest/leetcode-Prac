class Solution(object):
    def largestInteger(self, nums, k):
        if isinstance(nums, int) and isinstance(k, (list, tuple)):
            nums, k = k, nums

        n = len(nums)
        subarray_counts = defaultdict(int)

        for i in range(n - k + 1):
            sub = set(nums[i : i + k])
            for val in sub:
                subarray_counts[val] += 1

        ans = -1
        for val, count in subarray_counts.items():
            if count == 1 and val > ans:
                ans = val

        return ans