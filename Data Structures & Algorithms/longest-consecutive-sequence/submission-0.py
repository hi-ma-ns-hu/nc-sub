class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check if current nums[i] is start of the sequence
        max_len = 0
        seen = set()
        for num in nums:
            curr = num
            length = 1
            if (num-1) not in seen:
                seen.add(num)
                length = 1
            
            while curr+1 in nums:
                curr = curr+1
                length += 1
            max_len = max(max_len, length)

        return max_len