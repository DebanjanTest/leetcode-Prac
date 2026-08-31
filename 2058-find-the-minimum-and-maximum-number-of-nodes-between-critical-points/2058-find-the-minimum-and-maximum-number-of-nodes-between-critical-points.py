# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

  def nodesBetweenCriticalPoints(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: List[int]
    """
    if not head or not head.next or not head.next.next:
      return [-1, -1]

    first_idx = -1
    last_idx = -1
    prev_idx = -1
    min_dist = float("inf")

    prev = head
    curr = head.next
    idx = 1

    while curr.next:
      nxt = curr.next
      if (curr.val > prev.val and curr.val > nxt.val) or (
          curr.val < prev.val and curr.val < nxt.val
      ):
        if first_idx == -1:
          first_idx = idx
        else:
          min_dist = min(min_dist, idx - prev_idx)
        prev_idx = idx
        last_idx = idx

      prev = curr
      curr = nxt
      idx += 1

    if first_idx == -1 or first_idx == last_idx:
      return [-1, -1]

    return [min_dist, last_idx - first_idx]