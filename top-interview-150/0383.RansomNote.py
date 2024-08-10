class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomFreq = {}
        magazineFreq = {}
        for char in ransomNote:
            ransomFreq[char] = 1 + ransomFreq.get(char, 0)
        for char in magazine:
            magazineFreq[char] = 1 + magazineFreq.get(char, 0)
        for char in ransomFreq:
            if char not in magazineFreq:
                return False
            if ransomFreq[char] > magazineFreq[char]:
                return False
        return True
