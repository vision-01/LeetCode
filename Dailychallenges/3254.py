

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        results = []
        for i in range(n-k+1):
            c=True
            lm=nums[i]
            for j in range(i+1,i+k):
                if(nums[j]>lm):
                    lm=nums[j]
                if(nums[j]-nums[j-1]!=1): 
                    c=False
                    results.append(-1)
                    break
            if(c):
                results.append(lm)
        return results
            

            
# class Solution:
#     def resultsArray(self, nums: List[int], k: int) -> List[int]:
#         if k == 1: return nums
#         ans = []
#         l, r = 0, 1
#         n = len(nums)

#         while r < n:
#             if nums[r] - nums[r-1] != 1:
#                 while l < r and l + k - 1 < n:
#                     ans.append(-1)
#                     l+=1
#                 l = r
#             elif r - l == k - 1:
#                 ans.append(nums[r])
#                 l += 1

#             r += 1
#         return ans