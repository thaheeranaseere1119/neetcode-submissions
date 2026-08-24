class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = x**2 + y**2
            heapq.heappush(minheap, (dist, point))
        result = []
        for i in range(k):
            result.append(heapq.heappop(minheap)[1])
        return result

        