class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        color = 1
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "1":
                    color += 1
                    self.colorAround(x, y, color, grid)
        return color - 1
    
    def colorAround(self, x: int, y: int, color: int, grid: List[List[str]]):
        grid[y][x] = color
        if x != 0 and grid[y][x - 1] == "1":
            self.colorAround(x - 1, y, color, grid)
        if x != len(grid[y]) - 1 and grid[y][x + 1] == "1":
            self.colorAround(x + 1, y, color, grid)
        if y != 0 and grid[y - 1][x] == "1":
            self.colorAround(x, y - 1, color, grid)
        if y != len(grid) - 1 and grid[y + 1][x] == "1":
            self.colorAround(x, y + 1, color, grid)
            
        
#Solution using disjoint set (a.k.a union find)
class UF:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        self.size = [1] * size
        self.parents = {i for i in range(size)}
        
    def find(self, index: int) -> int:
        root = index
        while root != self.parent[root]:
            root = self.parent[root]
        
        while index != root:
            temp = self.parent[index]    
            self.parent[index] = root
            index = temp
        
        return root
            
    def union(self, set1: int, set2: int):
        a = self.find(set1)
        b = self.find(set2)
        if a == b:
            return
        
        self.parent[b] = self.parent[a]
        self.size[a] += self.size[b]
        self.parents.remove(b)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        totalcol = len(grid[0])
        totalrow = len(grid)
        disjoint_set = UF(totalcol * totalrow)
        for row, row_item in enumerate(grid):
            for col, col_item in enumerate(row_item):
                if row < totalrow - 1 and grid[row + 1][col] == col_item:
                    disjoint_set.union(row * totalcol + col, (row + 1) * totalcol + col)
                if col < totalcol - 1 and grid[row][col + 1] == col_item:
                    disjoint_set.union(row * totalcol + col, row * (totalcol) + (col + 1))
        result = 0
        for item in disjoint_set.parents:
            x = item % totalcol
            y = item // totalcol
            if grid[y][x] == "1":
                result += 1
        return result
                        
                    