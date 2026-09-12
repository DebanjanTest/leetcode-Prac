import bisect


class Solution(object):

  def maximumWeight(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[int]
    """
    n = len(intervals)
    events = sorted([(r, l, w, i) for i, (l, r, w) in enumerate(intervals)])
    end_times = [e[0] for e in events]

    dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

    for i in range(1, n + 1):
      r, l, w, orig_idx = events[i - 1]
      p = bisect.bisect_left(end_times, l)

      for k in range(5):
        dp[i][k] = dp[i - 1][k]

      for k in range(1, 5):
        prev_w, prev_idxs = dp[p][k - 1]
        cand_w = prev_w + w
        cand_idxs = sorted(prev_idxs + [orig_idx])

        best_w, best_idxs = dp[i][k]
        if cand_w > best_w or (cand_w == best_w and cand_idxs < best_idxs):
          dp[i][k] = (cand_w, cand_idxs)

    best_weight = 0
    best_indices = []

    for k in range(1, 5):
      cand_w, cand_idxs = dp[n][k]
      if cand_w > best_weight or (
          cand_w == best_weight and cand_idxs < best_indices
      ):
        best_weight = cand_w
        best_indices = cand_idxs

    return best_indices