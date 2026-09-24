class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        if num_rows == 0: # Empty grid
            return 0
        num_cols = len(grid[0])
        number_of_islands = 0
        map = grid.copy()

        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                if map[row_idx][col_idx] == '0':
                    continue
                number_of_islands += 1
                map[row_idx][col_idx] = '0' # Mark as visited
                self._bfs(map, row_idx, col_idx)
        return number_of_islands

    def _bfs(self, map: List[List[int]], row_idx: int, col_idx: int) -> None:
        '''
        Traverse neighbors and mark them as visited
        '''
        neighbors = [(row_idx, col_idx)] # queue for BFS
        while neighbors:
            row, col = neighbors.pop(0)
            # Check horizontally and vertically with boundaries constraints
            ## Horizontally
            if row - 1 >= 0 and map[row-1][col] == '1':
                map[row-1][col] = '0' # Visited
                neighbors.append((row-1,col))
            if row + 1 < len(map) and map[row+1][col] == '1':
                map[row+1][col] = '0' # Visited
                neighbors.append((row+1,col))
            ## Vertically
            if col - 1 >= 0 and map[row][col-1] == '1':
                map[row][col-1] = '0' # Visited
                neighbors.append((row,col-1))
            if col + 1 < len(map[0]) and map[row][col+1] == '1':
                map[row][col+1] = '0' # Visited
                neighbors.append((row,col+1))