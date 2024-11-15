from timecomplexity import estimate_time_complexity

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        v = n - 1
        result = x
        bit_position = 0
        while v > 0:
            if (x & (1 << bit_position)) == 0:
                if (v & 1) == 1:
                    result |= (1 << bit_position)
                v >>= 1
            bit_position += 1
        
        return result
