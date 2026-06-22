class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = list()
        res = list()
        for i, v in enumerate(nums):
            heapq.heappush(heap, (-v, i))

            # before pushing check if current top is out of window length, if yes pop it
            while heap[0][1] <= i-k:
                heapq.heappop(heap)

            # push to the result once window length exceeds or equals k
            if i >= k-1:
                res.append(-heap[0][0])

        return res