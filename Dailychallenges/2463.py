from typing import List
from functools import cache
import math

class Solution:
    def minimumTotalDistance(self, robots: List[int], factories: List[List[int]]) -> int:
        @cache
        def dp(r_idx, f_idx):
            if r_idx == len(robots):
                return 0
            if f_idx == len(factories):
                return math.inf
          
            result = dp(r_idx, f_idx + 1)
            total_dist = 0
          
            for unit in range(factories[f_idx][1]):
                if r_idx + unit == len(robots):
                    break
                total_dist += abs(robots[r_idx + unit] - factories[f_idx][0])
                result = min(result, total_dist + dp(r_idx + unit + 1, f_idx + 1))
          
            return result

        robots.sort()
        factories.sort(key=lambda x: x[0])
        ans = dp(0, 0)
        dp.cache_clear()
        return ans
