class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, tfreq = {}, {}
        start, end, front = 0, 0, 0
        minlen = float("inf")
        for char in t:
            tfreq[char] = 1 + tfreq.get(char, 0)
        have, need = 0, len(tfreq)
        while end < len(s):
            char = s[end]
            window[char] = 1 + window.get(char, 0)
            if char in tfreq and tfreq[char] == window[char]:
                have += 1
            while have == need and start <= end:
                if (end - start + 1) < minlen:
                    minlen = end - start + 1
                    front = start
                lchar = s[start]
                window[lchar] -= 1
                if lchar in tfreq and window[lchar] < tfreq[lchar]:
                    have -= 1
                start += 1
            end += 1
        return "" if minlen == float("inf") else s[front:front+minlen]
