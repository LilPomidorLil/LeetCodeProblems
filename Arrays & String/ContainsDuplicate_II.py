# https://leetcode.com/problems/contains-duplicate-ii/

#Given an integer array nums and an integer k, return true if there are two distinct indices i and j
# in the array such that nums[i] == nums[j] and abs(i - j) <= k.

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mdict = {}

        for i, digit in enumerate(nums):
            if digit in mdict and (i - mdict[digit]) <= k:
                return True
            else:
                mdict[digit] = i
        return False

if __name__ == '__main__':
    obj = Solution()
    nums = [1,2,3,1,2,3]
    k = 2
    print(obj.containsNearbyDuplicate(nums, k))