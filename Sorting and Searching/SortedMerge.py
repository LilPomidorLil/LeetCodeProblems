# https://leetcode.com/problems/merge-sorted-array/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        u_p, d_p, r_p = m - 1, n - 1, nums1.__len__() - 1

        while d_p >= 0:
            if u_p >= 0 and nums2[d_p] <= nums1[u_p]:
                nums1[r_p] = nums1[u_p]
                nums1[u_p] = 0
                u_p -= 1
                r_p -= 1
            else:
                nums1[r_p] = nums2[d_p]
                d_p -= 1
                r_p -= 1

if __name__ == '__main__':
    obj = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    obj.merge(nums1, m, nums2, n)