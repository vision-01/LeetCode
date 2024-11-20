# from typing import List


# class Solution:
#     def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
#         n=len(nums)
#         ss=n
#         maxidx=nums.index(max(nums))
#         left=maxidx-1
#         right=maxidx+1
#         leftval=0
#         rightval=0
#         or_till_now=nums[maxidx]
#         max_or_till_now=0
#         if(or_till_now>=k):
#             return 1
        
#         while left>=0 or right<n:            
#             if left>=0:
#                 leftval=or_till_now|nums[left]
#             if right<n:
#                 rightval=or_till_now|nums[right]
#             if leftval>=rightval and left>=0:
#                 or_till_now=leftval
#                 left-=1
#             elif right<n and rightval>=leftval:
#                 or_till_now=rightval
#                 right+=1
#             print(left,right,or_till_now)
#             if(or_till_now>=k):
#                 ss=right-left-1

#                 max_or_till_now=max(max_or_till_now,or_till_now)
#                 break
            
                
#         if(max_or_till_now<k):
#             return -1
#         return ss

# print(Solution().minimumSubarrayLength([2,1,9,12,1,2,1], 21))

            
# print(89|26|12|2|1|62)
class Solution:
    def minimumSubarrayLength(self, nums, k):
        n = len(nums)
        bitSetCount = [0] * 32
        ot_till_now = 0
        start_index = 0
        m = float('inf')
        
        for end_index in range(n):
            ot_till_now |= nums[end_index]
            
            for bit in range(32):
                if nums[end_index] & (1 << bit):
                    bitSetCount[bit] += 1
            
            while start_index <= end_index and ot_till_now >= k:
                m = min(m, end_index - start_index + 1)
                
                updatedOR = 0
                for bit in range(32):
                    if nums[start_index] & (1 << bit):
                        bitSetCount[bit] -= 1
                    if bitSetCount[bit] > 0:
                        updatedOR |= (1 << bit)
                
                ot_till_now = updatedOR
                start_index += 1
        
        return m if m != float('inf') else -1