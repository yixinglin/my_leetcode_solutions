"""
LeetCode 5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #return self.brutal(s)
        return self.expandAroundCenter(s)

    """   方法1， 枚举所有可能      """
    def brutal(self, s):
        maxlen = 0
        begin = 0
        end = 0
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                length = j - i + 1
                if (length > maxlen):
                    if (self.__isPalindromic(s, i, j)):
                        if length >maxlen:
                            maxlen = length
                            begin = i
                            end = j
        return s[begin:end+1]

    def __isPalindromic(self, s, begin, end):
        i = begin
        j = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    """   方法2，中心扩散法  """
    def expandAroundCenter(self, s):
        L = len(s)
        length = 0
        start = 0
        for i in range(L):
            l = max(self.__getLen(s, i, i, L),  # odd
                        self.__getLen(s, i, i + 1, L)) # even
            if (length < l):
                length = l
                start = i - (length//2 - (length+1) % 2)
        return s[start: start + length]

    def __getLen(self, s, left, right, L):
        """
        Get length of the palindromic substring
        :param s: original string
        :param left:  left index
        :param right: right index
        :param L: length of s
        """
        while (left >= 0 and right < L and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1

    """   方法3，动态规划法  """



string = "baabad"
string = "cbbd"
#string = "ac"
res = Solution().longestPalindrome(string)
print(res)
