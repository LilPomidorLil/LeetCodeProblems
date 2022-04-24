# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, nums.__len__() - 1

        while l <= r:
            m = (l + r) // 2

            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[m] == target:
                return  m

            if nums[l] <= nums[m]:
                if nums[l] <= target and target <= nums[m]:
                    r = m -1
                else:
                    l = m + 1
            else:
                if nums[m] <= target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1



if __name__ == '__main__':
    obj = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 5
    print(obj.search(nums, target))