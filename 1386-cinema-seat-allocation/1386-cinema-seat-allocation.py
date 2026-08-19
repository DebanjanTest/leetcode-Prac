class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        occupied = collections.defaultdict(int)
        for r, c in reservedSeats:
            if 1 < c < 10:
                occupied[r] |= (1 << c)

        LEFT = 60
        RIGHT = 960
        MID = 240

        ans = 2 * (n - len(occupied))
        for mask in occupied.values():
            left = (mask & LEFT) == 0
            right = (mask & RIGHT) == 0
            if left and right:
                ans += 2
            elif left or right or ((mask & MID) == 0):
                ans += 1

        return ans