class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, n in enumerate(nums):
            if not stack or n < nums[stack[-1]]:
                stack.append(i)
        
        max_width = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                max_width = max(max_width, j - stack.pop())
        
        return max_width