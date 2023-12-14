class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        row_ones = [0 for i in range(m)]
        col_ones = [0 for i in range(n)]

        for i in range(m):
            for j in range(n):
                row_ones[i] += grid[i][j]
                col_ones[j] += grid[i][j]
        
        diff = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(2*row_ones[i] + 2*col_ones[j] - m - n)
            diff.append(row)
        return diff