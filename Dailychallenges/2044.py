class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        count = 0

        def backtrack(i, current_or):
            nonlocal max_or, count
            if i == len(nums):
                if current_or > max_or:
                    max_or = current_or
                    count = 1
                elif current_or == max_or:
                    count += 1
                return

            # Include nums[i]
            backtrack(i + 1, current_or | nums[i])
            # Exclude nums[i]
            backtrack(i + 1, current_or)

        backtrack(0, 0)
        return count
