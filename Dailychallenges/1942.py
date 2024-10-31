import heapq
from typing import List

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        
        friends = sorted([(times[i][0], times[i][1], i) for i in range(n)])
        
        available_chairs = []
        
        for i in range(n):
            heapq.heappush(available_chairs, i)
        
        leaving_heap = []
        
        for arrival, leaving, friend_idx in friends:
            
            while leaving_heap and leaving_heap[0][0] <= arrival:
                _, chair = heapq.heappop(leaving_heap)
                heapq.heappush(available_chairs, chair)
            
            chair = heapq.heappop(available_chairs)
            
            if friend_idx == targetFriend:
                return chair
            
            heapq.heappush(leaving_heap, (leaving, chair))
