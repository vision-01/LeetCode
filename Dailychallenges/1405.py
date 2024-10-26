class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        counts = [('a', a), ('b', b), ('c', c)]
        while True:
            counts.sort(key=lambda x: -x[1])
            for char, count in counts:
                if count > 0 and (len(result) < 2 or result[-1] != char or result[-2] != char):
                    result.append(char)
                    counts[counts.index((char, count))] = (char, count - 1)
                    break
            else:
                break

        return ''.join(result)
        
        
        