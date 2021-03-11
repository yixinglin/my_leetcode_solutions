#include<vector>
#include <iostream>
#include "tools.h"
#include <climits>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        return method1(nums1, nums2);
    }

    // Method 1, O(m+n)
    double method1(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size(), len2 = nums2.size();
        vector<int> sorted_nums(len1 + len2, 0);
        int i=0, j=0, k=0;
        while (i < len1 || j < len2) {
            int ni = i<len1? nums1[i]: INT_MAX;
            int nj = j<len2? nums2[j]: INT_MAX;
            if (ni <= nj) {
                sorted_nums[k++] = ni;
                i += 1;
            } else {
                sorted_nums[k++] = nj;
                j += 1;
            }
        }
        int length = len1 + len2;
        if (length % 2 == 0) {
            i = length / 2;
            return (sorted_nums[i] + sorted_nums[i - 1]) / 2.0;
        } else {
            i = (length - 1) / 2;
            return sorted_nums[i];
        }
    }
};


int main()
{
    cout << "Hello world!" << endl;
    //int arr1[4] = {1,2,5,8};
    //int arr2[4] = {3,4,6};
    vector<int> nums1 = {1,2,5,8};
    vector<int> nums2 = {3,4,6};
    //array2vector(arr1, nums1, int(4));
    print_vector(nums1);
    //array2vector(arr2, nums2, 3);
    print_vector(nums2);
    double res = Solution().findMedianSortedArrays(nums1, nums2);
    cout <<res;
    return 0;
}
