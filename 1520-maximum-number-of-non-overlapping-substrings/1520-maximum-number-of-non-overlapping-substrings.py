class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []
        for ch in first:
            l = first[ch]
            r = last[ch]
            valid = True
            i = l
            while i <= r:
                c = s[i]
                if first[c] < l:
                    valid = False
                    break
                r = max(r, last[c])
                i += 1
            if valid:
                intervals.append((r, l))

        intervals.sort()
        res = []
        prev_r = -1
        for r, l in intervals:
            if l > prev_r:
                res.append(s[l : r + 1])
                prev_r = r

        return res