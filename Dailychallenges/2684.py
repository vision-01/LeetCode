from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_moves = 0
        
        def dfs(row, col, memo):
            if (row, col) in memo:
                return memo[(row, col)]
            
            moves = 0
            for dr, dc in [(-1, 1), (0, 1), (1, 1)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] > grid[row][col]:
                    moves = max(moves, 1 + dfs(new_row, new_col, memo))
            
            memo[(row, col)] = moves
            return moves
        
        for i in range(m):
            max_moves = max(max_moves, dfs(i, 0, {}))
        
        return max_moves