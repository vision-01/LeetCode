class Solution(object):
    def maximumBeauty(self, items, queries):
        
        inf = float('inf')
        bb = [[0, 0, inf]]
        
        items.sort(key=lambda x: x[0])

        for p, b in items:
            lb = bb[-1]
            if b > lb[1]:
                bb[-1][2] = p
                bb.append([p, b, inf])

        res = []

        for q in queries:
            for i in range(len(bb) - 1, -1, -1):
                if bb[i][0] <= q:
                    res.append(bb[i][1])
                    break

        return res