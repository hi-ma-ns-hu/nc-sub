class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = list()
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break

            # escape i duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i+1, len(nums)-1

            while j < k:
                if nums[j]+nums[k] == -1*nums[i]:
                    res.append([nums[i], nums[j], nums[k]])
                    # escape j and k duplicates
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
                elif nums[j]+nums[k] > -1*nums[i]:
                    k -= 1
                else:
                    j += 1
        return res