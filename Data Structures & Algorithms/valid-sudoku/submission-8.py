class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSeen = {i: set() for i in range(9)}
        colSeen = {i: set() for i in range(9)}
        squareSeen = {i: set() for i in range(9)}

        def addToSeen(i,j,cell):
            rowSeen[i].add(cell)
            colSeen[j].add(cell)
            r = (0,3)
            setNum = 0 
            added = False
            while r[0] < 9: 
                c = (0,3)
                while c[0] < 9: 
                    if r[0] <= i < r[1] and c[0] <= j < c[1]:
                        squareSeen[setNum].add(cell)
                        added = True 
                        break 
                    setNum += 1
                    c = (c[0] + 3, c[1]+3)
                if added: 
                    break
                r = (r[0] + 3, r[1] + 3)

        def inSeen(i,j,cell):
            if cell in rowSeen[i]: 
                return True
            if cell in colSeen[j]:
                return True
            r = (0,3)
            setNum = 0 
            while r[0] < 9: 
                c = (0,3)
                while c[0] < 9: 
                    if r[0] <= i < r[1] and c[0] <= j < c[1]:
                        return cell in squareSeen[setNum]
                    setNum += 1
                    c = (c[0] + 3, c[1]+3)
                r = (r[0] + 3, r[1] + 3)
            print("should never get here")
            return False            

        for i in range(9):
            for j in range(0,9):
                cell = board[i][j]
                if not cell == '.':
                    if not self.isDigit(cell):
                        return False 
                    if inSeen(i,j,cell):
                        return False

                addToSeen(i,j,cell)

        return True

    def isDigit(self, value: str) -> bool:
        valid = len(value) == 1 and "0" <= value <= "9"
        return valid
