from collections import deque


class Solution(object):

  def minMoves(self, classroom, energy):
    """
    :type classroom: List[str]
    :type energy: int
    :rtype: int
    """
    m, n = len(classroom), len(classroom[0])
    litter_map = {}
    litter_count = 0
    start_pos = 0

    for r in range(m):
      for c in range(n):
        cell = classroom[r][c]
        if cell == "S":
          start_pos = r * n + c
        elif cell == "L":
          litter_map[r * n + c] = 1 << litter_count
          litter_count += 1

    target_mask = (1 << litter_count) - 1
    if target_mask == 0:
      return 0

    # Precompute adjacent transitions for speed
    graph = [[] for _ in range(m * n)]
    for r in range(m):
      for c in range(n):
        if classroom[r][c] == "X":
          continue
        u = r * n + c
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
          nr, nc = r + dr, c + dc
          if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != "X":
            v = nr * n + nc
            is_reset = classroom[nr][nc] == "R"
            litter_bit = litter_map.get(v, 0)
            graph[u].append((v, is_reset, litter_bit))

    total_states = (m * n) << litter_count
    max_energy = [-1] * total_states

    start_idx = start_pos << litter_count
    max_energy[start_idx] = energy

    q = deque([(start_pos, energy, 0)])
    steps = 0

    while q:
      for _ in range(len(q)):
        pos, e, mask = q.popleft()

        if mask == target_mask:
          return steps

        if e == 0:
          continue

        for npos, is_reset, lbit in graph[pos]:
          ne = energy if is_reset else e - 1
          nmask = mask | lbit
          state_idx = (npos << litter_count) | nmask

          if ne > max_energy[state_idx]:
            max_energy[state_idx] = ne
            q.append((npos, ne, nmask))

      steps += 1

    return -1