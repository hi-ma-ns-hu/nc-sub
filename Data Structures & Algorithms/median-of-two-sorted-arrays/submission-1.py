class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1)+len(nums2)

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # run binary search on smaller
        l, r = 0, len(nums1)
        while True: 
            m = (l+r)//2 # number of items from nums1
            n = (length//2)-m-2 # number of items from nums1

            nums1_left = nums1[m] if m >= 0 else float('-infinity')
            nums1_right = nums1[m+1] if (m+1) < len(nums1) else float('infinity')
            nums2_left = nums2[n] if n >= 0 else float('-infinity')
            nums2_right = nums2[n+1] if (n+1) < len(nums2) else float('infinity')

            # check if left and right partition using both nums1 and nums2 are formed correctly
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # check if odd
                if length % 2:
                    return min(nums1_right, nums2_right)
                return (max(nums1_left, nums2_left)+min(nums1_right, nums2_right))/2
            elif nums1_left > nums2_right:
                r = m-1
            else:
                l = m+1