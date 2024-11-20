class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        tsum=[]
        l=0
        prevsum=0
        for r in range(n):
            prevsum+=nums[r]
            if r-l+1>k:
                prevsum-=nums[l]
                l+=1
            if(r-l+1==k):
                tsum.append(prevsum)
        return tsum