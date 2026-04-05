class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row, column, square = {}, {}, {}
        for r in range(len(board)):
            for c in range(len(board[r])):
                number = board[r][c]
                if number == '.':
                    continue

                if r not in row:
                    row[r] = []
                if number in row[r]:
                    return False
                row[r].append(number)

                if c not in column:
                    column[c] = []
                if number in column[c]:
                    return False
                column[c].append(number)

                subtree = (r // 3) * 3 + (c // 3)
                if subtree not in square:
                    square[subtree] = []
                if number in square[subtree]:
                    return False
                square[subtree].append(number)
            
            if r == 3:
                print(f'This is row: {row}')
                print(f'This is column: {column}')
                print(f'This is subtree: {square}')

        return True
