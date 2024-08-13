class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtracking(lc, rc, pattern):
            if lc == rc == n:
                ans.append(pattern)
                return
            if lc < n:
                backtracking(lc + 1, rc, pattern + "(")
            if lc > rc:
                backtracking(lc, rc + 1, pattern + ")")
        backtracking(0,0,"")
        return ans
