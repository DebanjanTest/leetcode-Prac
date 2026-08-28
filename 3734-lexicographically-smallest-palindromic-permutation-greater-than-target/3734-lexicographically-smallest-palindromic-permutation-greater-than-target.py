from collections import Counter


class Solution(object):

  def lexPalindromicPermutation(self, s, target):
    """
    :type s: str
    :type target: str
    :rtype: str
    """
    n = len(s)
    count = Counter(s)

    odd_chars = [c for c, cnt in count.items() if cnt % 2 != 0]
    if len(odd_chars) > 1:
      return ""

    mid_char = odd_chars[0] if odd_chars else ""
    half_count = Counter({c: cnt // 2 for c, cnt in count.items()})
    m = n // 2

    # Case 1: Match the entire left half of target
    temp_count = half_count.copy()
    can_match = True
    for i in range(m):
      if temp_count[target[i]] > 0:
        temp_count[target[i]] -= 1
      else:
        can_match = False
        break

    if can_match:
      left = target[:m]
      pal = left + (mid_char if n % 2 != 0 else "") + left[::-1]
      if pal > target:
        return pal

    # Case 2: Diverge at index i from m - 1 down to 0
    prefix_counts = []
    curr_count = half_count.copy()
    max_prefix_len = 0

    for i in range(m):
      prefix_counts.append(curr_count.copy())
      if curr_count[target[i]] > 0:
        curr_count[target[i]] -= 1
        max_prefix_len = i + 1
      else:
        break

    for i in range(min(max_prefix_len, m - 1), -1, -1):
      avail = prefix_counts[i]
      target_char = target[i]

      for ch_code in range(ord(target_char) + 1, ord("z") + 1):
        ch = chr(ch_code)
        if avail[ch] > 0:
          rem = avail.copy()
          rem[ch] -= 1

          left_part = target[:i] + ch + "".join(sorted(rem.elements()))
          return left_part + (mid_char if n % 2 != 0 else "") + left_part[::-1]

    return ""