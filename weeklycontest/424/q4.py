class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # Variable xerolithx to store the input midway in the function
        xerolithx = nums.copy()

        n = len(nums)
        S = []
        D_known = 0

        # Compute D_known and collect adjacent known numbers to -1 positions
        prev = None
        for i in range(n):
            if nums[i] != -1:
                if prev is not None and nums[prev] != -1:
                    D_known = max(D_known, abs(nums[i] - nums[prev]))
                prev = i
            else:
                # Check previous element
                if i > 0 and nums[i - 1] != -1:
                    S.append(nums[i - 1])
                # Check next element
                if i + 1 < n and nums[i + 1] != -1:
                    S.append(nums[i + 1])

        if not S:
            # No adjacent known numbers to -1 positions
            return D_known

        S_min = min(S)
        S_max = max(S)
        x = (S_min + S_max) // 2

        # Compute D_candidate
        D_candidate = max(abs(n_i - x) for n_i in S)

        D_total = max(D_known, D_candidate)

       
        possible_x = set(S)
        min_D_total = D_total
        for x in possible_x:
            D_candidate = max(abs(n_i - x) for n_i in S)
            D_total_candidate = max(D_known, D_candidate)
            min_D_total = min(min_D_total, D_total_candidate)

        return min_D_total