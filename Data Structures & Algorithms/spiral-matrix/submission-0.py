class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        '''
        1. Go right until len
        2. Go down until len
        3. Go left until len
        4. Go up until len - 1
        5. Repeat 1 - 5 for unvisited elements/coords
                     j
          i .  .  .  .
            .  .  .  .
            .  .  .  .
            
        '''
        if not matrix or len(matrix) == 0:
            return []

        rows = len(matrix)
        cols = len(matrix[0])
        limits = {
            'right': cols - 1,
            'down': rows - 1,
            'left': 0,
            'up': 0,
        }
        spiral = []
        
        while len(spiral) < rows*cols:
            # Right
            for col in range(limits['left'], limits['right'] + 1):
                spiral.append(matrix[limits['up']][col])
            # Down
            for row in range(limits['up'] + 1, limits['down'] + 1):
                spiral.append(matrix[row][limits['right']])
            # Left
            if limits['up'] != limits['down']:
                for col in range(limits['right'] - 1, limits['left'] - 1, -1):
                    spiral.append(matrix[limits['down']][col])
            # Up
            if limits['left'] != limits['right']:
                for row in range(limits['down'] - 1, limits['up'], -1):
                    spiral.append(matrix[row][limits['left']])
            
            limits['left'] += 1
            limits['up'] += 1
            limits['right'] -= 1
            limits['down'] -= 1

        return spiral