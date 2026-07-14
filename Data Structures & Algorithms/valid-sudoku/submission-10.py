class SeenSet: 
    def __init__(self):
        self.rowSeen = {i: set() for i in range(9)}
        self.colSeen = {i: set() for i in range(9)}
        self.squareSeen = {i: set() for i in range(9)}

    def add(self,i,j,cell):
        self.rowSeen[i].add(cell)
        self.colSeen[j].add(cell)

        r = (0,3)
        setNum = 0 
        while r[0] < 9: 
            c = (0,3)
            while c[0] < 9: 
                if r[0] <= i < r[1] and c[0] <= j < c[1]:
                    self.squareSeen[setNum].add(cell)
                    return
                setNum += 1
                c = (c[0] + 3, c[1]+3)
            r = (r[0] + 3, r[1] + 3)

    def inSet(self,i,j,cell):
        if cell in self.rowSeen[i]: 
            return True
        if cell in self.colSeen[j]:
            return True 

        r = (0,3)
        setNum = 0 
        while r[0] < 9: 
            c = (0,3)
            while c[0] < 9: 
                if r[0] <= i < r[1] and c[0] <= j < c[1]:
                    return cell in self.squareSeen[setNum]
                setNum += 1
                c = (c[0] + 3, c[1]+3)
            r = (r[0] + 3, r[1] + 3)
        return False

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenSet = SeenSet()

        for i in range(9):
            for j in range(0,9):
                cell = board[i][j]
                if not cell == '.':
                    if not self.isDigit(cell):
                        return False 
                    if seenSet.inSet(i,j,cell):
                        return False

                seenSet.add(i,j,cell)

        return True

    def isDigit(self, value: str) -> bool:
        valid = len(value) == 1 and "0" <= value <= "9"
        return valid
