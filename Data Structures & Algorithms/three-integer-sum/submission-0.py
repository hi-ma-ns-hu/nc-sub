class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(f'nums {nums}')
        k = len(nums)-1
        res = list()
        for i in range(len(nums)-2):
            j = i+1
            print(f'i {i}, j {j}, k {k}')
            while j < k:
                print(f'j {j}, k {k}, i+j {nums[j]+nums[k]} -i {-1*nums[i]}')
                if nums[j]+nums[k] == -1*nums[i]:
                    res.append([nums[i], nums[j], nums[k]])
                    break
                elif nums[j]+nums[k] > -1*nums[i]:
                    k -= 1
                else:
                    j += 1
        print(f'res {res}')
        return res