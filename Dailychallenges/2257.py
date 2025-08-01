class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        grid = [['U'] * n for _ in range(m)] 
        for r, c in walls:
            grid[r][c] = 'W' 
        for r, c in guards:
            grid[r][c] = 'G'  

        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        
        for gr, gc in guards:
            for dr, dc in directions:
                r, c = gr + dr, gc + dc
                while 0 <= r < m and 0 <= c < n and grid[r][c] != 'W' and grid[r][c] != 'G':
                    if grid[r][c] == 'U':
                        grid[r][c] = 'S'  
                    r += dr
                    c += dc

        
        count = 0
        for row in grid:
            for cell in row:
                if cell == 'U':
                    count += 1

        return count