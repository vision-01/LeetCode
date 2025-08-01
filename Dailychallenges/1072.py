class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        ans=0
        for i in range(n):
            cnt=0
            for j in range(n):
                if matrix[i]==matrix[j] or matrix[i]==[1-x for x in matrix[j]]:
                    cnt+=1
            ans=max(ans,cnt)
        return ans
        