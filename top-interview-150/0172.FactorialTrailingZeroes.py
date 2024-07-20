class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        c = 0
        while n > 0:
            n //= 5
            c += n
        return c
