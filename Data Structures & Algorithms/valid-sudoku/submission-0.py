class Solution:
    def check_list_duplicates(self, lst: list) -> bool:
        nums = [num for num in lst if num != "."]
        return len(nums) == len(set(nums)) 
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.check_list_duplicates(row):
                return False

        for col_ind in range(9):
            col = [row[col_ind] for row in board]
            if not self.check_list_duplicates(col):
                return False

        for row_ind_start in range(0, 9, 3):
            for col_ind_start in range(0, 9, 3):
                box = []
                for row in board[row_ind_start:row_ind_start + 3]:
                    for col_ind in range(col_ind_start, col_ind_start + 3):
                        box.append(row[col_ind])
                
                if not self.check_list_duplicates(box):
                    return False
        
        return True
