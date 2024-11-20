from typing import List


class Solution:
    def canFindTwoIncreasingSubarrays(self, inc, k, n):
        for i in range(0, n - 2 * k + 1):
            if inc[i] >= k and inc[i + k] >= k:
                return True
        return False

    def maxIncreasingSubarrays(self, nums):
        n = len(nums)
        inc = [1] * n

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc[i] = inc[i + 1] + 1

        left, right, result = 1, n // 2, 0

        while left <= right:
            mid = left + (right - left) // 2
            if self.canFindTwoIncreasingSubarrays(inc, mid, n):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result


print(Solution().maxIncreasingSubarrays([-19,-20,9,10,11,12]))
        