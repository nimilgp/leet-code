class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxlen = 0
        hashset = set()
        while r != len(s):
            if s[r] not in hashset:
                hashset.add(s[r])
                r += 1
            else:
                hashset.remove(s[l])
                l += 1
            maxlen = max(maxlen, r-l)
        return maxlen
