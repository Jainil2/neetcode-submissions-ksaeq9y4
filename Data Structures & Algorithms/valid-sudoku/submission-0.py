class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {i: set() for i in range(9)}
        col = {i: set() for i in range(9)}
        box = {i: set() for i in range(9)}
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':  
                    continue
                
                idx = (i // 3) * 3 + (j // 3)  
                
                if num in row[i] or num in col[j] or num in box[idx]:
                    return False
                
                row[i].add(num)
                col[j].add(num)
                box[idx].add(num)
        
        return True