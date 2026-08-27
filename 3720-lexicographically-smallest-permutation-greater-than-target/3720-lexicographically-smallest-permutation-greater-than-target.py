from collections import Counter


class Solution(object):

  def lexGreaterPermutation(self, s, target):
    """
    :type s: str
    :type target: str
    :rtype: str
    """
    n = len(s)
    count = Counter(s)

    prefix_counts = []
    curr_count = count.copy()
    max_prefix_len = 0

    for i in range(n):
      prefix_counts.append(curr_count.copy())
      if curr_count[target[i]] > 0:
        curr_count[target[i]] -= 1
        max_prefix_len = i + 1
      else:
        break

    for i in range(min(max_prefix_len, n - 1), -1, -1):
      avail = prefix_counts[i]
      target_char = target[i]

      for ch_code in range(ord(target_char) + 1, ord("z") + 1):
        ch = chr(ch_code)
        if avail[ch] > 0:
          rem = avail.copy()
          rem[ch] -= 1

          suffix = "".join(sorted(rem.elements()))
          return target[:i] + ch + suffix

    return ""