class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.compute(board, word)
    
    
    def compute(self, board: List[List[str]], word: str) -> bool:
        for rowi, row in enumerate(board):
            for chari, char in enumerate(row):
                if char == word[0:1]:
                    if self.checkaround(board, word[1:], [(rowi, chari)]):
                        return True
        
        return False
    
    def checkaround(self, board: List[List[str]], word:str, used:list) -> bool:
        if word == "":
            return True
        
        (y, x) = used[len(used) - 1]
        
        if y > 0 and board[y-1][x] == word[0:1] and (y-1, x) not in used:
            if self.checkaround(board, word[1:], used + [(y-1, x)]):
                return True
        
        if y < len(board) - 1 and board[y+1][x] == word[0:1] and (y+1, x) not in used:
            if self.checkaround(board, word[1:], used + [(y+1, x)]):
                return True
            
        if x > 0 and board[y][x-1] == word[0:1] and (y, x-1) not in used:
            if self.checkaround(board, word[1:], used + [(y, x-1)]):
                return True
            
        if x < len(board[y]) - 1 and board[y][x+1] == word[0:1] and (y, x+1) not in used:
            if self.checkaround(board, word[1:], used + [(y, x+1)]):
                return True
        
        return False
        
