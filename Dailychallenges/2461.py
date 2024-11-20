from typing import List
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        cntr=defaultdict(int)
        tsum=0
        prevsum=0
        l=0
        for r in range(n):
            prevsum+=nums[r]
            cntr[nums[r]]+=1
            if r-l+1>k:
                cntr[nums[l]]-=1
                if(cntr[nums[l]]==0):
                    cntr.pop(nums[l])
                prevsum-=nums[l]
                l+=1
            prevsum+=nums[r]
            tsum=max(tsum,prevsum)
            

# Example usage
solution = Solution()
print(solution.maximumSubarraySum([1,2,1,2,1], 2))  # Example input