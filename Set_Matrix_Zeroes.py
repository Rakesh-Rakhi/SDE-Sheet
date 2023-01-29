https://leetcode.com/problems/set-matrix-zeroes/
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c =[], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r.append(i)
                    c.append(j)
        for i in r:
            for x in range(len(matrix[0])):
                matrix[i][x] = 0
        for i in c:
            for x in range(len(matrix)):
                matrix[x][i] = 0
        
