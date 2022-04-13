# https://leetcode.com/problems/rotate-image/

#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

from typing import List

class Solution:
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     # будем делать поворот по 4 ячейкам, которые сначала образуют квадрат, затем мы идем вниз с точки зрения крайнего стобца
    #     # уменьшаем диапазон до нуля.
    #
    #
    #     n = len(matrix[0])
    #
    #     for i in range(n // 2 + n % 2): # такой диапазон обеспечит нам прохождение по верхней части матрицы (ее верхней половины)
    #         for j in range(n // 2): # это обеспечит нам проход до середины столбцов
    #             temporary = matrix[n - j - 1][i] # если идти по часовой стрелке, то это крайнее значение,
    #             # которое мы переместим в диаметрально противоположную ячейку, откуда начали движение
    #
    #             # нам нужно поменять 4 значения местами, сейчас напишем это правило !(начинать будем из нижнего правого угла)!
    #             matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
    #             matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
    #             matrix[j][n - i - 1] = matrix[i][j]
    #             matrix[i][j] = temporary

    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reflect(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]



if __name__ == '__main__':
    obj = Solution()
    obj.rotate([[1,2,3],[4,5,6],[7,8,9]])