class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_counts = Counter(tasks)
        heap = [-i for i in tasks_counts.values()]
        heapq.heapify(heap)     

        time = 0
        queue = deque() # [-count, time]

        while heap or queue:
            time += 1
            if heap:
                count = heapq.heappop(heap)+1
                if count:
                    queue.append([count, time+n])
            
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

        return time