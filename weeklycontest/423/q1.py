class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            if i + 2 * k - 1 < n:
                sub1 = nums[i:i + k]
                sub2 = nums[i + k:i + 2 * k]
                
                if all(sub1[j] < sub1[j + 1] for j in range(k - 1)) and \
                all(sub2[j] < sub2[j + 1] for j in range(k - 1)):
                    return True
        return False