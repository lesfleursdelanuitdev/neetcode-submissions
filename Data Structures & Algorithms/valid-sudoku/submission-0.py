class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.validRow(i,board):
                return False
            if not self.validCol(i, board):
                return False

        blocks = [(0,3),(3,6),(6,9)]
        for r in blocks:
            for c in blocks:
                if not self.validSquare(r,c,board):
                    return False

        return True

    def validSquare(self, r: (int,int), c: (int,int), board: List[List[str]]) -> bool:
        seen = {}
        for i in range(r[0],r[1]):
            for j in range(c[0],c[1]):
                cell = board[i][j]
                if not self.validChar(cell):
                    return False
                if cell in seen and not cell == '.':
                    return False
                seen[cell] = True
        return True


    def validRow(self, row: int, board: List[List[str]]) -> bool:
        return self.validDim(row,board,True)

    def validCol(self, col: int, board: List[List[str]]) -> bool: 
        return self.validDim(col,board,False)

    def validDim(self, j: int, board: List[List[str]], isRow: bool) -> bool:
        seen = {}
        for i in range(9):
            cell = board[j][i] if isRow else board[i][j]
            if not self.validChar(cell):
                return False
            if cell in seen and not cell == '.':
                return False
            seen[cell] = True
        return True

    def validChar(self, value: str) -> bool:
        return self.isDigit(value) or value == '.'

    def isDigit(self, value: str) -> bool:
        valid = len(value) == 1 and "0" <= value <= "9"
        return valid
