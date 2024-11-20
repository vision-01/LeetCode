class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        strt = 1 if (k>0) else 0
        end = k + 1 if(n>0) else k-1
        move = 1 if (k>0) else -1
        gsum=0
        for i in range(strt,end,move):
            gsum+=code[i]
        print(gsum)