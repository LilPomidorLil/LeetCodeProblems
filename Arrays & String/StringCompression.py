# https://leetcode.com/problems/string-compression/


# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.

# Это задача RLE, похожая была на курсе тренировок по алгоритмам

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        chars += [None]
        current_elem = chars[0]
        count = 0
        slow = 0

        for i, char in enumerate(chars):
            if char != current_elem:
                chars[slow] = current_elem
                current_elem = char
                slow += 1

                if count == 1:
                    continue

                for c in str(count):
                    chars[slow] = c
                    slow += 1

                count = 1

            elif char == current_elem:
                count += 1

        return slow
if __name__ == '__main__':
    obj = Solution()
    print(obj.compress(
["a","a","a","b","b","a","a"]))