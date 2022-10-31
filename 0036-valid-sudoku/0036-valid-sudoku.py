class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        square = collections.defaultdict(set) # key = (r / 3, c / 3)
        
        for r in range(9):
            for c in range(9):
                char = board[r][c] 
                if char == '.':
                    continue
                if (char in rows[r] or char in cols[c] or char in square[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])

        return True