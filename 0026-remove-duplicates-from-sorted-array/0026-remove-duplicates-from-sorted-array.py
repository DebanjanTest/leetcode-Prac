class Solution(object):
    def removeDuplicates(self, nums):
        off=0
        result=1
        cm=1
        n=len(nums)

        while (cm<n):
            if (nums[cm]==nums[cm-1]):
                cm+=1
                continue
            else:
                off+=1
                nums[off] = nums[cm]
                result+=1
                cm+=1

        return result

        """
        :type nums: List[int]
        :rtype: int
        """
        