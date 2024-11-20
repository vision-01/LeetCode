class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        dec = [0] * (n + 1)
        
        # Process each query to update the decrement array
        for l, r in queries:
            dec[l] += 1
            if r + 1 < n:
                dec[r + 1] -= 1
        
        # Apply the decrements to the original array
        cumulative = 0
        for i in range(n):
            cumulative += dec[i]
            nums[i] -= cumulative
        
        # Check if the array is a Zero Array
        return all(x <= 0 for x in nums)

#using cumulative sum to find the minimum number of queries to make the array zero
