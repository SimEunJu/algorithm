class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = []
        cols = []
        
        for i in range(0, n):
            rows.append(grid[0][i])
            cols.append(grid[i][0])
        
        for i in range(1, n):
            for j in range(0, n):
                rows[j] = max(rows[j], grid[i][j])
                cols[j] = max(cols[j], grid[j][i])
        
        sum = 0
        for i in range(0, n):
            for j in range(0, n):
               sum += min(rows[i], cols[j]) - grid[i][j]
        
        return sum
