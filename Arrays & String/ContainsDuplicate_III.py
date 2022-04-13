# https://leetcode.com/problems/contains-duplicate-iii/

#Given an integer array nums and two integers k and t, return true if there are two distinct indices i and j in the
# array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.

from typing import List

# TODO: finish execution in next time

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        buckets = {}

        for i in range(len(nums)):
            bucket_label = nums[i] // (t + 1)

            if bucket_label in buckets:
                return True

            buckets[bucket_label] = nums[i]


if __name__ == '__main__':
    obj = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    t = 0
    obj.containsNearbyAlmostDuplicate(nums, k, t)
