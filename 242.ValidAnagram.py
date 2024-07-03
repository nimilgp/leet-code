class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = {}
        for c in s:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        for c in t:
            if c not in chars:
                return False
            elif chars[c] == 0:
                return False
            else:
                chars[c] -= 1
        return True
