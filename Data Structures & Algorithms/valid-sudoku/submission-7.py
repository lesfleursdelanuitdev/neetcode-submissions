class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSeen = {i: set() for i in range(9)}
        colSeen = {i: set() for i in range(9)}
        for i in range(9):
            for j in range(0,9):
                cell = board[i][j]
                if not cell == '.':
                    if not self.isDigit(cell):
                        return False 
                    if cell in rowSeen[i]:
                        return False
                    if cell in colSeen[j]:
                        return False

                rowSeen[i].add(cell)
                colSeen[j].add(cell)

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

    def validDim(self, r: (int,int), c: (int,int), board: List[List[str]]) -> bool:
        seen = {}
        for i in range(r[0],r[1]):
            for j in range(c[0],c[1]):
                cell = board[i][j]
                if not self.isDigit(cell) and not cell == '.':
                    return False 
                if cell in seen and not cell == '.':
                    return False
                seen[cell] = True
        return True

    def isDigit(self, value: str) -> bool:
        valid = len(value) == 1 and "0" <= value <= "9"
        return valid
