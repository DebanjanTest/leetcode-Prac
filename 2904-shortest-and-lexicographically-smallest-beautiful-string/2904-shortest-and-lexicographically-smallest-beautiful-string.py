class Solution(object):

  def shortestBeautifulSubstring(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    ones = [i for i, ch in enumerate(s) if ch == "1"]

    if len(ones) < k:
      return ""

    best = ""

    for i in range(len(ones) - k + 1):
      start = ones[i]
      end = ones[i + k - 1] + 1
      candidate = s[start:end]

      if not best:
        best = candidate
      elif len(candidate) < len(best):
        best = candidate
      elif len(candidate) == len(best) and candidate < best:
        best = candidate

    return best