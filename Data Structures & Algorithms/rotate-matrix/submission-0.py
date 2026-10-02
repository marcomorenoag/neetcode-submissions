class Solution:
    def _transpose(self, matrix: list[list[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def _reflect(self, matrix: list[list[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                matrix[i][j], matrix[i][len(matrix) - 1 - j] = matrix[i][len(matrix) - 1 - j], matrix[i][j]

    
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        [[15,13,2,5],[9,4,8,10],[1,3,6,7],[11,14,12,16]]
        """
        # n = len(matrix)
        # rotated_m = []
        # for i in range(n):
        #     row = []
        #     for j in range(n - 1, -1, -1):
        #         row.append(matrix[j][i])
        #     rotated_m.append(row)

        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j] = rotated_m[i][j]
        self._transpose(matrix)
        self._reflect(matrix)
