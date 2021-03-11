#include <iostream>
#include <string>
#include<unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    unordered_map<string, vector<string>> state_table = {
        // state_name => input character [+/-, number, white space, other]
        {"start", {"signed", "number", "start", "end"}}, //next state
        {"end", {"end", "end", "end", "end"}},
        {"signed", {"end", "number", "end", "end"}},
        {"number", {"end", "number", "end", "end"}}
    };

public:
    int myAtoi(string s) {
        long long ans = 0;
        bool sign = 1;
        string state = "start";

        for(char c: s) {
            int index = __charType(c);
            state = state_table[state][index];
            if (state == "number")
                ans = ans * 10 + int(c - '0');
            else if (state == "end")
                break;
            else if (state == "signed")
                sign = c == '-' ? 0: 1;
            if(ans > (long long)INT_MAX)
                break;
        }
        if (sign == 0)  // negative
            return max(-ans, (long long)INT_MIN);
        else
            return min(ans, (long long) INT_MAX);
    }

private:
    int __charType(char c) {
        if (c == '+' || c == '-')
            return 0;
        else if(c == ' ')
            return 2;
        else if (c >= '0' && c <= '9')
            return 1;
        else // other
            return 3;
    }


};

int main()
{
    string test_str[7] = {"42",
    "   -42",
    "4193 with words",
    "words and 987",
    "-+91283472332a",
    "20000000000000000000",
    "-91283472332"};
    Solution s = Solution();
    int sol = s.myAtoi(test_str[5]);
    cout <<sol;
    return 0;
}
