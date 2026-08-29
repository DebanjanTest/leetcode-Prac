class Solution(object):

  def lexicographicallySmallestArray(self, nums, limit):
    """
    :type nums: List[int]
    :type limit: int
    :rtype: List[int]
    """
    n = len(nums)
    sorted_pairs = sorted((val, idx) for idx, val in enumerate(nums))

    res = [0] * n
    i = 0

    while i < n:
      j = i + 1
      while j < n and sorted_pairs[j][0] - sorted_pairs[j - 1][0] <= limit:
        j += 1

      group = sorted_pairs[i:j]
      indices = sorted(idx for val, idx in group)

      for k in range(len(group)):
        res[indices[k]] = group[k][0]

      i = j

    return res