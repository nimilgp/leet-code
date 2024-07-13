class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            hashmap = set()
            for j in range(9):
                element = board[i][j]
                if element == "." :
                    continue
                elif element not in hashmap:
                    hashmap.add(element)
                else:
                    return False
        for i in range(9):
            hashmap = set()
            for j in range(9):
                element = board[j][i]
                if element == "." :
                    continue
                elif element not in hashmap:
                    hashmap.add(element)
                else:
                    return False 
        for i in range(0,7,3):
            for j in range(0,7,3):
                hashmap = set()
                for k in range(9):
                    element = board[i+(k//3)][j+(k%3)]
                    if element == "." :
                        continue
                    elif element not in hashmap:
                        hashmap.add(element)
                    else:
                        return False     
        return True
