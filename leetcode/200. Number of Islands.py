class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)  # search adjacent lands
                    islands += 1
        return islands

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return  # exit condition

        grid[i][j] = "0"
        self.dfs(grid, i, j + 1)  # east
        self.dfs(grid, i, j - 1)  # west
        self.dfs(grid, i + 1, j)  # south
        self.dfs(grid, i - 1, j)  # north
