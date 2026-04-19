class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(f'nums {nums}')
        k = len(nums)-1
        res = list()
        for i in range(len(nums)-2):
            # escape i duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            print(f'i {i}, j {j}, k {k}')
            while j < k:
                print(f'j {j}, k {k}, i+j {nums[j]+nums[k]} -i {-1*nums[i]}')
                if nums[j]+nums[k] == -1*nums[i]:
                    arr = [nums[i], nums[j], nums[k]]
                    res.append(arr)

                    if nums[j] == nums[j+1]:
                        j += 1
                    if nums[k] == nums[k-1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
                elif nums[j]+nums[k] > -1*nums[i]:
                    k -= 1
                else:
                    j += 1
        print(f'res {res}')
        return res