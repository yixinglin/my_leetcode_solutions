"""
Longest Common Subsequence
LeetCode 1143
https://www.youtube.com/watch?v=ASoaQq66foQ&ab_channel=BackToBackSWE

Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.


Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
"""
import numpy as np

class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      memo = np.zeros([len(text2), len(text1)], dtype = int) -1 # cache
      res = self.lcs(text1, text2, memo)
      #res = self.cache(text1, text2)
      return res

    def lcs(self, s1, s2, memo):
      """
      Using recursion
      :param s1: String 1
      :param s2: String 2
      :param memo: cache. Note: if you don't use this cache, runtime may be extremely long
      :return:
      """
      m = len(s1)
      n = len(s2)
      if n>0 and m>0 and memo[n-1, m-1] != -1:
        return memo[n-1, m-1]

      if len(s1) == 0 or len(s2) == 0:  # empty string
        return 0

      if s1[-1] == s2[-1]:  # the last characters are the same,
        memo[n-1, m-1] = 1 + self.lcs(s1[0:-1], s2[0:-1], memo)
        return memo[n-1, m-1]  # crop the string
      else:
        r1 = self.lcs(s1[0:-1], s2, memo)
        r2 = self.lcs(s1, s2[0:-1], memo)
        memo[n-1, m-1] = max(r1, r2)
        return memo[n-1, m-1]


    def cache(self, text1, text2):
      """
      Cache, using DP table.
      :param text1: String 1
      :param text2: String 2
      :return:
      """
      n = len(text1) + 1
      m = len(text2) + 1
      cache = np.zeros([m, n], dtype= int)

      for i in range(1, n):
        for j in range(1, m):
          if text1[i-1] != text2[j-1]:
            cache[j, i] = max(cache[j-1, i], cache[j, i-1])
          else:
            cache[j, i] = cache[j-1, i-1] + 1  # use the previous result.

      return cache[m-1, n-1]


if __name__ == "__main__":
  #str1 = "abbc"
  #str2 = "ab"

  #str1 = "AGGTAB"
  #str2 = "GXTXAYB"

  #str1 = "ylqpejqbalahwr"
  #str2 = "yrkzavgdmdgtqpg"

  str1 = "ezupkr"
  str2 = "ubmrapg"
  res = Solution().longestCommonSubsequence(str1, str2)
  print("result", res)
