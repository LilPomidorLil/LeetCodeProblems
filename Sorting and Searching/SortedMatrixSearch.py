# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List

class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     l, r, m = 0, matrix.__len__() - 1, -1
    #
    #     while l <= r:
    #         m = (l + r) // 2
    #
    #         if matrix[m][0] == target:
    #             return True
    #
    #         if matrix[m][0] < target:
    #             l = m + 1
    #         else:
    #             r = m - 1
    #
    #     left, right = 0, matrix[r].__len__() - 1
    #
    #     while left <= right:
    #         med = (left + right) // 2
    #
    #         if matrix[r][med] == target:
    #             return True
    #
    #         if matrix[r][med] < target:
    #             left = med + 1
    #         else:
    #             right = med - 1
    #     return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = matrix.__len__(), matrix[0].__len__()

        def convet_ind(mid):
            return mid // n, mid % n

        l, r = 0, m*n - 1

        while l <= r:
            mid = (l + r) // 2

            i, j = convet_ind(mid)

            if matrix[i][j] == target:
                return True

            if matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1



if __name__ == '__main__':
    obj = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 20

    print(obj.searchMatrix(matrix, target))
