import sys
MAX_INT = sys.maxsize
MIN_INT = -MAX_INT

class Solution:

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        return self.sol_2(nums1, nums2)


    # sol_2 O(log m)  二分法
    def sol_2(self, nums1, nums2):
        LenA, LenB = len(nums1), len(nums2)
        Len = LenA + LenB
        # 保证数组1短于数组2
        if LenA > LenB:  # 交换数组
            nums2, nums1 = nums1, nums2
            LenA, LenB = LenB, LenA

        # 极端情况
        if LenA == 0:
            return  (nums2[(LenB - 1) // 2] + nums2[LenB // 2])/2

        startA = 0
        endA = LenA
        while startA <= endA:
            splitA = (startA + endA)//2 # A分割线左边元素数量
            splitB = (Len+1) // 2 - splitA #保证左边比右边多一个元素
            L1 = MIN_INT if splitA == 0 else nums1[splitA-1]  #分割线左边的元素
            R1 = MAX_INT if splitA == LenA else nums1[splitA] #分割线右边的元素
            L2 = MIN_INT if splitB == 0 else nums2[splitB-1] #分割线左边的元素
            R2 = MAX_INT if splitB == LenB else nums2[splitB] #分割线右边的元素

            print(splitA, splitB)

            if L1 > R2:
                endA = splitA -1 #分割线左移
            elif L2 > R1:
                startA = splitA +1 #分割线右移  ????
            else:  #结果
                if Len % 2==0: # 偶数
                    return (max(L1, L2) + min(R1, R2))/2
                else:
                    return max(L1, L2)

    # sol_1 O(m+n)
    def sol_1(self, nums1, nums2):
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


#list2 = [2,4,6,7,10]
# list1 = [1,3,5,8,9,11,12,13,14]
#list1 = [1,3,5,8,9,11,12,13,14]

list1 = [2]
list2 = [1]

res = Solution().findMedianSortedArrays(list1, list2)   # build a linked list
print(res)