class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.helper(board, 0, 0)
        
    def helper(self, board, y, x):
        for curY in range(y, 9):
            for curX in range(0, 9):
                if board[curY][curX] == ".":
                    for attempt in range(1,10):
                        if self.isValid(board, curY, curX, str(attempt)):
                            board[curY][curX] = str(attempt)
                            if self.helper(board, curY, curX):
                                return True
                            board[curY][curX] = "."
                    return False
        return True
    
    def isValid(self, board, y, x, attempt):
        curRow = board[y]
        for element in curRow:
            if element == attempt:
                return False
        for element in board:
            if element[x] == attempt:
                return False
        myX = -1
        if x < 3:
            myX = 0
        elif x != 0 and x < 6:
            myX = 1
        else:
            myX = 2
            
        myY = -1   
        if y < 3:
            myY = 0
        elif y != 0 and y < 6:
            myY = 1
        else:
            myY = 2
        
        myX *= 3
        myY *= 3
        for curY in range(myY, myY + 3):
            for curX in range(myX, myX + 3):
                if board[curY][curX] == attempt:
                    return False
        return True
                
        