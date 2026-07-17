class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k        
        self.streams = nums
        heapq.heapify(nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.streams, val)
        return self.streams[-self.k]