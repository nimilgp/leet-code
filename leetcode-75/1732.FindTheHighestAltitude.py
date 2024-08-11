class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h = 0
        altmax = 0
        for g in gain:
            h += g
            altmax = max(altmax, h)
        return altmax
