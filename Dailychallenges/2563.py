from typing import List

    class Solution:
        def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
            nums.sort()
            n = len(nums)
            count = 0
            
            for i in range(n):
                left = i + 1
                right = n - 1
                
                # Find the first index where nums[i] + nums[left] >= lower
                while left <= right:
                    mid = (left + right) // 2
                    if nums[i] + nums[mid] >= lower:
                        right = mid - 1
                    else:
                        left = mid + 1
                start = left
                
                left = i + 1
                right = n - 1
                
                # Find the last index where nums[i] + nums[right] <= upper
                while left <= right:
                    mid = (left + right) // 2
                    if nums[i] + nums[mid] <= upper:
                        left = mid + 1
                    else:
                        right = mid - 1
                end = right
                
                if start <= end:
                    count += end - start + 1
            
            return count

# Example usage
solution = Solution()
print(solution.countFairPairs([0, 1, 7, 4, 4, 5], 3, 6))  # Output: 6
print(solution.countFairPairs([1, 7, 9, 2, 5], 11, 11))  # Output: 1