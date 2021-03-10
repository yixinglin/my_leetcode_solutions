import sys
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        sorted_nums = list()
        len1 = len(nums1)
        len2 = len(nums2)
        i = 0
        j = 0
        while i < len1 or j < len2:
            ni = nums1[i] if i < len1 else sys.maxsize
            nj = nums2[j] if j < len2 else sys.maxsize
            if ni <= nj:
                sorted_nums.append(ni)
                i += 1
            else:
                sorted_nums.append(nj)
                j += 1

        print(sorted_nums)
        length = len1 + len2

        if length % 2 == 0:  # even
            i = length // 2
            return (sorted_nums[i] + sorted_nums[i - 1]) / 2.0
        else:  # odd
            i = (length - 1) // 2
            return sorted_nums[i]


list1 = [1, 2, 5, 8]
list2 = [3, 4, 6]


res = Solution().findMedianSortedArrays(list1, list2)   # build a linked list
print(res)