from typing import List
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Initialize prefix sum array
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
        result = n + 1  # Initialize result with a value larger than any possible subarray length
        dq = deque()  # Monotonic queue to store indices
        
        for i in range(n + 1):
            # Check for valid subarrays ending at index i
            while dq and prefix_sums[i] - prefix_sums[dq[0]] >= k:
                result = min(result, i - dq.popleft())
            # Maintain the deque to have increasing prefix sums
            while dq and prefix_sums[i] <= prefix_sums[dq[-1]]:
                dq.pop()
            dq.append(i)
        
        return result if result <= n else -1