class Solution:
    def isHappy(self, n: int) -> bool:
        def getSquared(num):
            ans = 0
            while(num>0):
                digit = num%10
                num = num//10
                ans += digit**2
            return ans
        visited = set()
        while n!=1:
            if n in visited:
                return False
            else:
                visited.add(n)
            n = getSquared(n)
        return True
