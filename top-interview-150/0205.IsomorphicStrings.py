class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        rosetta = {}
        taken = set()
        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]
            if char1 not in rosetta:
                if char2 in taken:
                    return False
                else:
                    rosetta[char1] = char2
            else:
                if rosetta[char1] != char2:
                    return False
            taken.add(char2)
        return True
