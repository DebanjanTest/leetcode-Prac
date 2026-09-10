class Solution(object):
    def merge(self, nums1, m, nums2, n):
        res = [0] * (m + n)
        id = 0
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res[id] = nums1[i]
                id += 1
                i += 1
            else:
                res[id] = nums2[j]
                id += 1
                j += 1

        while i < m:
            res[id] = nums1[i]
            id += 1
            i += 1

        while j < n:
            res[id] = nums2[j]
            id += 1
            j += 1

        for k in range(m + n):
            nums1[k] = res[k]