import re
from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l=len(arr)
        left=0
        right=l-1
        while left<l-1 and arr[left]<=arr[left+1]:
            left+=1
        if left==l-1:
            return 0
        
        while right>0 and arr[right]>=arr[right-1]:
            right-=1
        ans=min(l-left-1,right)

        i=0
        j=right
        while i<=left and j<l:
            if arr[i]<=arr[j]:
                ans=min(ans,j-i-1)
                i+=1
            else:
                j+=1
        return ans
    
        

        