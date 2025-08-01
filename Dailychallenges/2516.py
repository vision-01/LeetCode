from collections import defaultdict

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        ct = {'a': 0, 'b': 0, 'c': 0}
        
        for ch in s:
            ct[ch] += 1
        
        if any(ct[ch] < k for ch in 'abc'):
            return -1
        
        ma = {ch: ct[ch] - k for ch in 'abc'}
        
        ciw = {'a': 0, 'b': 0, 'c': 0}
        mwl = 0
        l = 0
        
        for r in range(n):
            ch = s[r]
            ciw[ch] += 1
            
            while any(ciw[ch] > ma[ch] for ch in 'abc'):
                ciw[s[l]] -= 1
                l += 1
            
            cwl = r - l + 1
            mwl = max(mwl, cwl)
        
        return n - mwl
