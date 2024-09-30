from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixset = set()
        mxlen = 0
        for i in arr1:
            x = str(i)
            st = ""
            for j in range(len(x)):
                st = st + x[j]
                prefixset.add(st)
        for i2 in arr2:
            x = str(i2)
            st = ""
            for j in range(len(x)):
                st = st + x[j]
                if st in prefixset:
                    xl = len(st)
                    if xl > mxlen:
                        mxlen = xl
        return mxlen
