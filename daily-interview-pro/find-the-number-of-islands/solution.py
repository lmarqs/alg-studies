class Solution(object):
    def inRange(self, grid, r, c):
        return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])

    def isLand(self, grid, r, c):
        return self.inRange(grid, r, c) and grid[r][c] == 1

    def removeIsland(self, grid, r, c):
        if self.isLand(grid, r, c):
            grid[r][c] = 0

            self.removeIsland(grid, r - 1, c)
            self.removeIsland(grid, r + 1, c)
            self.removeIsland(grid, r, c - 1)
            self.removeIsland(grid, r, c + 1)

    def numIslands(self, grid):
        counter = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if self.isLand(grid, r, c):
                    counter += 1
                    self.removeIsland(grid, r, c)

        return counter
