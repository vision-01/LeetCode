class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n=len(nums)
        ans=[]
        xor=0
        for i in range(n):
            xor^=nums[i]
            ans.append((2**maximumBit-1)^xor)
        return ans[::-1]