class Solution:
    def minimumPushes(self, word: str) -> int:
        l = len(word)
        ans = 0
        i = 1
        limit = l // 8
        
        while i <= limit:
            ans += i * 8
            i += 1
            
        ans += i * (l % 8)
        return ans