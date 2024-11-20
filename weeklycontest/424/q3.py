class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)
        
        def can_make_zero(k):
            diff = [0] * (n + 1)
            # Process each query up to k to update the difference array
            for idx in range(k):
                l, r, vali = queries[idx]
                diff[l] += vali
                if r + 1 < n:
                    diff[r + 1] -= vali
            
            # Apply the decrements to the original array
            cumulative = 0
            for i in range(n):
                cumulative += diff[i]
                if cumulative < nums[i]:
                    return False
            return True
        
        left, right = 0, q
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if can_make_zero(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result if result != -1 else -1
    
#using binary search to find the minimum number of queries to make the array zero