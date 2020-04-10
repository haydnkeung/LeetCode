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
            
        