class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row = {}
        column = {}

        for r in grid:
            row[tuple(r)] = row.get(tuple(r), 0) + 1
        for j in range(len(grid[0])):
            c = []
            for i in range(len(grid)):
                c.append(grid[i][j])
            column[tuple(c)] = column.get(tuple(c), 0) + 1
        
        count = 0
        for r in row:
            if r in column:
                count += row[r] * column[r]
        return count