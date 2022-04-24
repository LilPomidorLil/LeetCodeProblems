# https://leetcode.com/problems/first-bad-version/

def isBadVersion(version: int) -> bool:
    if version >= 2:
        return True
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m -1
            else:
                l = m +1
        return l


if __name__ == '__main__':
    obj = Solution()
    n = 5
    print(obj.firstBadVersion(n))