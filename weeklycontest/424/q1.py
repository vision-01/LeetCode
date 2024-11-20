from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def simulate(curr, direction):
            n = len(nums)
            nums_copy = nums[:]
            while 0 <= curr < n:
                if nums_copy[curr] == 0:
                    curr += direction
                elif nums_copy[curr] > 0:
                    nums_copy[curr] -= 1
                    direction = -direction
                    curr += direction
            return all(x == 0 for x in nums_copy)
        
        valid_selections = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if simulate(i, 1):  # Move right
                    valid_selections += 1
                if simulate(i, -1):  # Move left
                    valid_selections += 1
        
        return valid_selections

# Example usage
solution = Solution()
print(solution.countValidSelections([0, 1, 2, 0]))  # Example input
