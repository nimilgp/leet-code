class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        i = 0
        c = min(len(word1),len(word2))
        while i<c:
            ans = ans + word1[i] + word2[i]
            i += 1
        if len(word1) > len(word2):
            return ans + word1[i:]
        else:
            return ans + word2[i:]
