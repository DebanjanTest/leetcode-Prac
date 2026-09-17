class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        min_len = [float('inf')] * (n + 1)
        
        prefix_sum = 0
        pos = {0: -1}
        ans = float('inf')
        
        for j in range(n):
            prefix_sum += arr[j]
            pos[prefix_sum] = j
            
            min_len[j] = min_len[j - 1]
            
            need = prefix_sum - target
            if need in pos:
                i = pos[need]
                curr_len = j - i
                min_len[j] = min(min_len[j], curr_len)
                
                if i >= 0 and min_len[i] != float('inf'):
                    ans = min(ans, curr_len + min_len[i])
                    
        return ans if ans != float('inf') else -1