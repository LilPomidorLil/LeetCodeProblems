# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mdict = {}

        for digit in nums:
            if digit in mdict:
                return digit
            else:
                mdict[digit] = 1


if __name__ == '__main__':
    obj = Solution()
    nums = [1, 3, 4, 2, 2]
    obj.findDuplicate(nums)