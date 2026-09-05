class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        hash_set = set()
        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]: continue
            for i, v in enumerate(trip):
                if v == target[i]: hash_set.add(i)
        
        return len(hash_set) == 3