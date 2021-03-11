class Solution:
    def minOperations(self, nums1: list, nums2: list) -> int:

        # case 0: no solution? no need to calculate?


        # case 1: having solution
        """
            assume len1 < len2
            assume s1 < s2
            1. sorting nums1 and nums2
            2. calculate diff
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            len1, len2 = len2, len1


        if len1*6 < len2*1:
            return -1  # no solution

        s1 = sum(nums1)
        s2 = sum(nums2)
        if s1 == s2:
            return 0

        if s1 > s2: # assume s1 < s2
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1

        cnt = 0
        nums1 = sorted(nums1, reverse=False)
        nums2 = sorted(nums2, reverse=True)
        len1 = len(nums1)
        len2 = len(nums2)
        i = 0; j = 0
        while (s1 != s2):
            diff = abs(s2 - s1)
            d1 = 6-nums1[i] if i < len1 else 0
            d2 = nums2[j] - 1 if j < len2 else 0
            d = min(max(d1, d2), diff)
            #print(d)
            if d1 >= d2:
                s1 += d
                i += 1
            else:
                s2 -= d
                j += 1
            cnt += 1
        return cnt