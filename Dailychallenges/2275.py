class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count=0
        for i in range(32):
            localmax=0
            for j in range(len(candidates)):
                if candidates[j]&(1<<i):
                    localmax+=1
            count=max(count,localmax)
        return count


        