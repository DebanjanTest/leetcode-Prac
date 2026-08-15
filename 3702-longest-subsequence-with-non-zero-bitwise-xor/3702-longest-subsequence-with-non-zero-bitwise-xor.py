class Solution(object):
    def longestSubsequence(self, nums):
        total_xor=0
        has_non_zero=False

        for x in nums:
            total_xor ^=x
            if x!=0:
                has_non_zero = True

        if not has_non_zero:
                return 0

        return len(nums) if total_xor != 0 else len(nums)-1
 