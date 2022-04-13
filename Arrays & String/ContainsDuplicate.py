# https://leetcode.com/problems/contains-duplicate/

#Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.


from typing import List

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         if len(set(nums)) == len(nums):
#             return False
#         else:
#             return True

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        up, down = 0, 0

        while True:
            if up == down == len(nums)-1:
                return False

            if up == down:
                down += 1

            if nums[up] == nums[down]:
                return True

            if nums[up] != nums[down]:
                up = down

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         mdict = {}
#
#         for num in nums:
#             if num in mdict:
#                 return True
#             else:
#                 mdict[num] = 0
#         return False

if __name__ == '__main__':
    obj = Solution()
    print(obj.containsDuplicate([1,2,3,4]))

