class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        # floyed hare-tortoise algo
        # when slow and fast meet break
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if nums[slow] == nums[fast]:
                break

        # init second slow pointer from beginning
        # when slow == slow2, the item at slow is bieng repeated
        slow2= 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if nums[slow] == nums[slow2]:
                return nums[slow]       