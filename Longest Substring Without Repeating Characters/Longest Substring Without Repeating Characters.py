class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_s = set()
        l = 0
        max_length = 0
        for i in range (len(s)):
            while s[i] in long_s:
                long_s.remove(s[l])
                l += 1
            long_s.add(s[i])               
            max_length = max(max_length, i-l+1)
        return max_length
            
