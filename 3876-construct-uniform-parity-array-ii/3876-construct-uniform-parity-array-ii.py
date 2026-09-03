class Solution(object):

  def uniformArray(self, nums1):
    """
    :type nums1: List[int]
    :rtype: bool
    """
    min_val = min(nums1)
    if min_val % 2 == 1:
      return True

    for x in nums1:
      if x % 2 == 1:
        return False

    return True