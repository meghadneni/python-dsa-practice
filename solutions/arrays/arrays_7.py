"""
Valid Sudoku
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true
"""
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #1.check row for duplicates
        #2. check col for duplicates
        # check 3x3 boxes - 0-2/3-5/6-8
        # when i%3 == 0 , j =i=0, run only for 3 rounds -> 
        # create three hash maps - One for row ,one for column, one for grid. For each row,col,grid - create a set of elements 
        # when iterating through grid elements, if element seen in any of these maps, return false . If not add to the map and continue.
        #Finally return true
        col = defaultdict(set)
        row = defaultdict(set)
        blk = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row[i] : 
                    return False
                if board[i][j] in col[j] :
                    return False
                if board[i][j] in blk[(i//3,j//3)]:
                    return False
                
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                blk[(i//3,j//3)].add(board[i][j])

        return True