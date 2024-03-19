class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            temp = [i for i in r if i != '.']
            if len(temp) != len(set(temp)):
                return False
        for i in range(9):
            temp = []
            for j in range(9):
                if board[j][i] != '.':
                    temp.append(board[j][i])
            if len(temp) != len(set(temp)):
                return False
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                temp = [i for i in square if i != '.']
                if len(temp) != len(set(temp)):
                    return False
        return True
