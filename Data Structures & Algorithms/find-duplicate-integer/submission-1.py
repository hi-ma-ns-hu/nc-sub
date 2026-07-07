class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        # floyd hare-tortoise algo
        # when slow and fast index meet break
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # init second slow pointer from beginning
        # when slow == slow2 in terms of index, the item at slow is bieng repeated, return the slow
        slow2= 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow       