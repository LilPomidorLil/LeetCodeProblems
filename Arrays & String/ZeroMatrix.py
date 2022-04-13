# https://leetcode.com/problems/set-matrix-zeroes/

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.
from typing import List

class Solution:
    # def setZeros(self, matrix: List[List[int]]) -> None:
    #     # пробежимся по всей матрице и найдем ее нули
    #
    #     ROW_SET = set()
    #     COL_SET = set()
    #
    #     ROW = len(matrix)
    #     COL = len(matrix[0])
    #
    #     for i in range(ROW):
    #         for j in range(COL):
    #             if matrix[i][j] == 0:
    #                 ROW_SET.add(i)
    #                 COL_SET.add(j)
    #
    #     # пробежимся еще раз по всей матрице и если эта строка или столбец есть в отмеченных выше,
    #     # то меняем значение на ноль
    #
    #     for i in range(ROW):
    #         for j in range(COL):
    #             if i in ROW_SET or j in COL_SET:
    #                 matrix[i][j] = 0

    def setZeros(self, matrix: List[List[int]]) -> None:
        ROW = len(matrix)
        COL = len(matrix[0])

        is_col = False

        for i in range(ROW):

            if matrix[i][0] == 0:
                is_col = True

            for j in range(COL):

                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, ROW):
            for j in range(1, COL):

                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for c in range(COL):
                matrix[0][c] = 0

        if is_col:
            for r in range(ROW):
                matrix[r][0] = 0

        print(*matrix, sep='\n')


if __name__ == '__main__':
    obj = Solution()
    print(*[[0,1,2,0],[3,4,0,2],[1,3,1,5]], sep = '\n', end = '\n\n')
    obj.setZeros([[0,1,2,0],[3,4,0,2],[1,3,1,5]])


