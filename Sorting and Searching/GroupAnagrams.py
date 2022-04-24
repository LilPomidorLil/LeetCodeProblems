# https://leetcode.com/problems/group-anagrams/

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mdict = {}

        for s in strs:
            key = "".join(sorted(s))

            if key not in mdict:
                mdict[key] = [s]
            else:
                mdict[key].append(s)

        return list(mdict.values())


if __name__ == '__main__':
    obj = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    obj.groupAnagrams(strs)