#include <iostream>
#include<vector>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        //return expandAroundCenter(s);
        return manacher(s);
    }

    string expandAroundCenter(const string &s) {
        const int L = s.size();
        int length = 0, start = 0, l;
        for (int i=0; i<L; ++i) {
            l = max(_getLen(s, i, i, L),  //odd
                    _getLen(s, i, i+1, L)); //even
            if(length<l) {
                length = l;
                start = i - (length/2 - (length+1) % 2);
            }
        }
        return s.substr(start, length);
    }

    int _getLen(const string &s, int left, int right, const int &L) {
        /*
        Get length of the palindromic substring
        :param s: original string
        :param left:  left index
        :param right: right index
        :param L: length of s
        */
        while (left >= 0 && right < L && s[left] == s[right]) {
            --left;
            ++right;
        }
        return right - left -1;
    }


    string manacher(const string &s) {
        int length = s.size();
        if (length < 2)
            return s;

        // 字符串预处理
        string new_str = "#";
        for(int i=0; i<length; ++i) {
            new_str += s[i];
            new_str += "#";
        }
        length = 2*length + 1;
        // 计算回文
        int max_right = 0, center = 0, maxlen = 1;
        int begin = 0, mirror = 0;
        vector<int> p(length, 0);  // p辅助数组

        for(int i=0; i<length; ++i) {
            // Case 1
            if (i < max_right) {
                mirror = 2*center - i;
                // case 1.1 and case 1.2.
                p[i] = min(max_right-i, p[mirror]);
            }

            // case 1.3 equal， 中心扩散
            // 或者 i > max_right 也中心扩散
            int right = i + p[i] + 1;
            int left = i - p[i] - 1;
            while(left >= 0 && right < length
                    && new_str[left] == new_str[right]) {
                left -= 1;
                right += 1;
                p[i] += 1;
            }

            // update center and max_right，重新以i为中心开始扩散计算
            if (i + p[i] > max_right) {
                max_right = i + p[i];
                center = i;
            }

            // update maxlen
            if (p[i] > maxlen) {
                maxlen = p[i];
                begin = (i-maxlen) / 2;
            }
        }

        return s.substr(begin, maxlen);
    }
};


int main()
{
    cout << "Hello world!" << endl;
    // string s = "baabad";
    string s = "baaabvbvvvvbwa";
    string str = Solution().longestPalindrome(s);
    cout <<str;

    return 0;
}
