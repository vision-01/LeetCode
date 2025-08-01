class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        abcnt=s.count("ab")
        bacnt=s.count("ba")
        ttl=0
        if(abcnt > bacnt):
            while "ab" in s:
                s = s.replace("ab", "", 1)
            ttl= abcnt * x+ y*s.count("ba")

        else:
            while "ba" in s:
                s = s.replace("ba", "", 1)
            ttl= bacnt * x+ y*s.count("ab")
        return ttl
