#include <iostream>
#include<vector>
#include<algorithm>
#include<numeric>
using namespace std;

void print_vector(vector<int>& nums) {
    for(int i=0; i < nums.size(); ++i) {
        cout << nums[i] << " ";
    }
    cout<<endl;
}

class Solution {
public:
    int minOperations(vector<int>& nums1, vector<int>& nums2) {
        // sort(begin(nums1), end(nums2));
        int len1 = nums1.size();
        int len2 = nums2.size();
        // Assume len1 < len2
        if (len1 > len2)
            swap(len1, len2);
        if (len1*6 < len2*1)  // no solution
            return -1;

        int s1 = accumulate(nums1.begin(), nums1.end(), 0);
        int s2 = accumulate(nums2.begin(), nums2.end(), 0);
        if (s1 == s2)
            return 0;
        // assume s1 < s2
        if (s1 > s2) {
            swap(nums1, nums2);
            swap(s1, s2);
        }

        int cnt = 0;
        sort(nums1.begin(), nums1.end());   // ascending order
        sort(nums2.begin(), nums2.end(), greater<int>()); //descending order
        len1 = nums1.size();
        len2 = nums2.size();
        int i=0, j=0;
        while (s1 != s2) {
            const int diff = abs(s2-s1);
            const int d1 = i<len1 ? 6-nums1[i]: 0;
            const int d2 = j<len2 ? nums2[j]-1 : 0;
            const int d = min(max(d1, d2), diff);

            if (d1 >= d2) {
                s1 += d;
                i += 1;
            } else {
                s2 -= d;
                j += 1;
            }
            cnt += 1;
        }
        return cnt;
    }
};



int main()
{

    vector<int> nums1 = {1,6,3,4,5,2};
    vector<int> nums2 = {1,1,2,2,2,2};
    int cnt = Solution().minOperations(nums1, nums2);
    //print_vector(nums1);
    cout << cnt;
    return 0;
}
