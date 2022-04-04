# https://leetcode.com/problems/permutation-in-string/


# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = collections.Counter(s1)
        count = len(s1)

        for i, char in enumerate(s2):
            if char in s1_dict:
                s1_dict[char] -= 1

                # знак не строгий, т.к. в коде не предусмотрено добавление назад
                if s1_dict[char] >= 0:
                    count -= 1

                # здесь мы начинаем смотреть назад и проверяем, были ли лишние буквы между перетасованной последовательностью
                # если такие были, то мы возвращаем назад в частотный словарь те буквы, которые оттуда были удалены и увеличиваем длину строки,
                # но только в том случае, если этот символ точно добавился (длина строки увеличилась на единицу)
                left_index = i - len(s1)

                if left_index >= 0 and s2[left_index] in s1_dict:
                    s1_dict[s2[left_index]] += 1

                    if s1_dict[s2[left_index]] > 0:
                        count += 1

                if count == 0:
                    return True
        return False


if __name__ == '__main__':
    obj = Solution()
    obj.checkInclusion(s1 = "abc", s2 = "aabpchuop")


