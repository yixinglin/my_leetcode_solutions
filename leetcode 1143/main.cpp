#include <iostream>

using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int n = text1.size();
        int m = text2.size();
        int cache[m+1][n+1] = {0};
        for(int i=0; i<n+1; i++)
            for(int j=0; j<m+1; j++) {
                if (i == 0 || j == 0) {
                    cache[j][i] = 0;
                    continue;
                }

                if (text1[i-1] == text2[j-1]) {
                    cache[j][i] = 1 + cache[j-1][i-1];   // found a match. plus 1
                } else {
                     cache[j][i] = max(cache[j][i-1], cache[j-1][i]);  // not a match
                }
            }
        return cache[m][n];
    }
};

int main()
{
    Solution sol = Solution();
    int res = sol.longestCommonSubsequence("abcb", "ab");
    cout<<res<<endl;
    return 0;
}
