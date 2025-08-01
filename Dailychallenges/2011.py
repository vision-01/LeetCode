from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        l=len(nums)
        lst=[]
        for i in range(l):
            mx=0
            rorval=0
            for j in range(i,l):
                rorval|=nums[j]
                if(rorval>mx):
                    mx=rorval
                    lst.append(j+1)
        return lst        
                    
