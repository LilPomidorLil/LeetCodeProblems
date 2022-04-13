# https://leetcode.com/problems/rotate-string/

#Given two strings s and goal, return true if and only if s can become goal after some number of shifts s.
#shift on s consists of moving the leftmost character of s to the rightmost position.

#For example, if s = "abcde", then it will be "bcdea" after one shift.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in (goal+goal)

if __name__ == '__main__':
    obj = Solution()

    s = "abc"
    goal = 'bca'

    print(obj.rotateString(s, goal))
