"""
1775. Equal Sum Arrays With Minimum Number of Operations
You are given two arrays of integers nums1 and nums2, possibly of different lengths.
The values in the arrays are between 1 and 6, inclusive.
In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.
Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2.
Return -1​​​​if it is not possible to make the sum of the two arrays equal.

Example 1:

Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
"""


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
            # print(nums1, nums2, i, j)
            print("nums1 = {}, i = {}; \nnums2 = {}, j = {}".format(nums1, i, nums2, j) )
            diff = abs(s2 - s1)  # avoid overflow
            d1 = 6-nums1[i] if i < len1 else 0
            d2 = nums2[j] - 1 if j < len2 else 0
            d = min(max(d1, d2), diff)   # calculate difference
            print("s1 = {0}, s2 = {1}, diff = {2}\n".format(s1, s2, d))
            # chose the largest difference
            if d1 >= d2:
                s1 += d
                nums1[i] += d
                i += 1
            else:
                s2 -= d
                nums2[j] -= d
                j += 1
            cnt += 1
        return cnt


if __name__ == "__main__":
    #nums1 = [1, 2, 3, 6, 5, 4]
    #nums2 = [1,1,2,2,2,2]

    #nums1 = [6,6]
    #nums2 = [1]

    nums1 = [5, 6, 4, 3, 1, 2]
    nums2 = [6, 3, 3, 1, 4, 5, 3, 4, 1, 3, 4]  # 4

    #nums1 = [1, 1, 1, 1, 1, 1, 1]
    #nums2 = [6]

    res = Solution().minOperations(nums1, nums2)
    print("result", res)
