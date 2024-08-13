class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        def backtracking(row, col, i):
            if i == len(word):
                return True
            if (row < 0 or col < 0 or
                row >= len(board) or 
                col >= len(board[0]) or 
                word[i] != board[row][col]
                or (row,col) in path):
                return False
            path.add((row,col))
            res =  backtracking(row+1, col, i+1) or backtracking(row, col+1, i+1) or backtracking(row-1, col, i+1) or backtracking(row, col-1, i+1) 
            path.remove((row,col))
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if  backtracking(i,j,0):
                    return True
        return False
