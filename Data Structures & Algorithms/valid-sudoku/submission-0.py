import logging
from typing import Final

_SUDOKU_SIZE: Final[int] = 9

class Solution:
    def _rows_are_valid(self, board: List[List[str]]) -> bool:
        for i in range(_SUDOKU_SIZE):
            visited_nums = set()
            row = board[i]
            for j in range(_SUDOKU_SIZE):
                try:
                    num = int(row[j])
                    if num in visited_nums:
                        return False
                    visited_nums.add(num)
                except:
                    continue
            logging.debug(f'visited_nums: {visited_nums} | ')
        logging.debug('=' * 30)
        return True


    def _cols_are_valid(self, board: List[List[str]]) -> bool:
        for i in range(_SUDOKU_SIZE):
            visited_nums = set()
            for j in range(_SUDOKU_SIZE):
                try:
                    col = board[j][i]
                    num = int(col)
                    if num in visited_nums:
                        return False
                    visited_nums.add(num)
                except:
                    continue
            logging.info(f'visited_nums: {visited_nums}')
        logging.info('=' * 30)
        return True
    
    def _subboxes_are_valid(self, board: List[List[str]]) -> bool:
        """
        subbox_num = 1
        pivot_row = 0
        pivot_col = 3
        """
        for subbox_num in range(_SUDOKU_SIZE):
            visited_nums = set()
            pivot_row = (subbox_num // 3) * 3
            pivot_col = (subbox_num * 3) % _SUDOKU_SIZE
            for i in range(pivot_row, pivot_row + 3):
                for j in range(pivot_col, pivot_col + 3):
                    try:
                        num = int(board[i][j])
                        if num in visited_nums:
                            return False
                        visited_nums.add(num)
                    except:
                        continue
            logging.warning(f'visited_nums: {visited_nums}')
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self._rows_are_valid(board) and self._cols_are_valid(board) and self._subboxes_are_valid(board)

def main() -> None:
    """
    [
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    visited_nums_in_row
    visited_nums_in_col
    visited_nums_in_subbox = set()

    ---
    NS:
    1. iterate thru all rows
    2. iterate thru all cols
    3. sliding window of 3x3 
    """
    #sol = Solution()

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    main()
        