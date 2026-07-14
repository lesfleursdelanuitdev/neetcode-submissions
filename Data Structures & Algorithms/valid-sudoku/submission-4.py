class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.validRow(i,board):
                return False
            if not self.validCol(i, board):
                return False

        r = (0,3)
        while r[0] < 9: 
            c = (0,3)
            while c[0] < 9: 
                if not self.validSquare(r,c,board):
                    return False
                c = (c[0] + 3, c[1]+3)
            r = (r[0] + 3, r[1] + 3)

        return True

    def validSquare(self, r: (int,int), c: (int,int), board: List[List[str]]) -> bool:
        return self.validDim(r,c,board)

    def validRow(self, row: int, board: List[List[str]]) -> bool:
        return self.validDim((row,row+1),(0,9),board)

    def validCol(self, col: int, board: List[List[str]]) -> bool: 
        return self.validDim((0,9),(col,col+1),board)

    def validDim(self, r: (int,int), c: (int,int), board: List[List[str]]) -> bool:
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

    def validChar(self, value: str) -> bool:
        return self.isDigit(value) or value == '.'

    def isDigit(self, value: str) -> bool:
        valid = len(value) == 1 and "0" <= value <= "9"
        return valid
