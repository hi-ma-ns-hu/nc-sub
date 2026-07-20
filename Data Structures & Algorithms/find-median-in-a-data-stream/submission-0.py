class MedianFinder:

    def __init__(self):
        # min is either left[0] or right[0] or mean(left[0]+right[0])
        self.max_heap = list() # for left half, we use max of left half which is left[0] for mean
        self.min_heap = list() # for right half, we use min of right half which is right[0] for mean

    def addNum(self, num: int) -> None:
        # push to max_heap or min_heap
        if self.max_heap and num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        # balance the max_heap and min_heap in case their length diff is > 1
        if len(self.min_heap) > len(self.max_heap)+1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        if len(self.max_heap) > len(self.min_heap)+1:
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -val)

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0]-self.max_heap[0])/2.0
        
        