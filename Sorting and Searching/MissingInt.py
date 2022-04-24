# https://leetcode.com/problems/missing-number/

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = nums.__len__()
        return int((n * (n + 1) / 2) - sum(nums))

if __name__ == '__main__':
    obj = Solution()
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(obj.missingNumber(nums))