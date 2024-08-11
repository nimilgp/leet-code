class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char != '*':
                stack.append(char)
            else:
                stack.pop()
        ans = ""
        for char in stack:
            ans += char
        return ans
