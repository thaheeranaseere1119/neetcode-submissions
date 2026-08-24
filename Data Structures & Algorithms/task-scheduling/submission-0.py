from collections import Counter, deque
import heapq

class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)

        heap = []

        for count in freq.values():
            heap.append(-count)

        heapq.heapify(heap)

        queue = deque()

        time = 0

        while heap or queue:

            time += 1

            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

            if heap:

                count = 1 + heapq.heappop(heap)

                if count:
                    queue.append((count, time + n + 1))

        return time