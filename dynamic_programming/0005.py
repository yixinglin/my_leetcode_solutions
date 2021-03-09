"""
LeetCode 5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""
from tools.timer import timer
class Solution:

    @timer
    def longestPalindrome(self, s: str) -> str:
        #return self.brutal(s)  # 33ms
        #return self.expandAroundCenter(s)  #0.0ms
        #return self.dynamicsProgramming(s)  # 54ms
        return self.manacher(s)

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

    """   方法3，动态规划法  
    时间复杂度 O(n^2)
    空间复杂度 O(n^2)
    动态规划是暴力解法的优化，枚举子串个数 O(n^2)
    """
    def dynamicsProgramming(self, s):

        length = len(s)
        dp = [[0 for i in range(length)] for j in range(length)]
        # initialize the dp table
        for i in range(length):
            dp[i][i] = True

        maxLen = 1
        begin = 0
        for j in range(length):
            for i in range(0, j):
                if s[i] != s[j]:  #  首尾字母不一样，必定不是回文
                    dp[i][j] = False
                else:  # 首尾字母一样
                    if j-i < 3:   # 且 内子串长度 (j-1) - (i+1) +1 <= 1
                        dp[i][j] = True
                    else:   # 且内子串是回文/不是回文，那么子串肯定是回文/不是回文
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] == True and j-i+1 > maxLen:
                    maxLen = j-i+1
                    begin = i

        return s[begin: begin+maxLen]

    """
    Manacher算法
    时间复杂度 O(n)
    空间复杂度 
    面试的时候不要求掌握
    """
    def manacher(self, s):
        length = len(s)
        if length < 2:
            return s

        # 字符预处理
        new_str = "#"
        for i in range(length):
            new_str += (s[i] + "#")
        length = len(new_str)

        # 计算回文
        max_right = 0
        center = 0
        maxlen = 1
        begin = 0

        p = [0 for _ in range(length)]   # 辅助数组，记录中心扩散的步数

        for i in range(length):
            # Case 1:
            if i < max_right:
                mirror = 2*center -i   # i关于center的对称
                # 利用center回文的对称性，来判断i的回文
                if p[mirror] < max_right - i:  # case 1.1， 利用以前的信息。利用center回文的对称性
                    p[i] = p[mirror]
                elif p[mirror] > max_right - i:  # case 1.2， 利用以前的信息
                    p[i] = max_right - i

            # case 1.3 equal, 中心扩散
            # 或者 i > max_right 也中心扩散
            right = i + p[i] + 1
            left = i - p[i] - 1
            while left >= 0 and right < length and new_str[left] == new_str[right]:
                left -= 1
                right += 1
                p[i] += 1

            # update center and max_right，重新以i为中心开始扩散计算
            if i + p[i] > max_right:
                max_right = i + p[i]
                center = i

            # update maxlen
            if p[i] > maxlen:
                maxlen = p[i]
                begin = (i-maxlen) // 2

        return s[begin: begin + maxlen]



string = "baabad"
#string = "cbbd"
#string = "ac"
#string = "b"
#string = "abcda"
#string = "yzwhuvljgkbxonhkpnxldwkaiboqoflbotqamsxyglfqniflcrtsxbsxlwmxowwnnxychyrjedlijejqzsgwakzohghpxgamecmhcalfoyjtutxeciwqupwlxrgdcpfvybskrytvmwkvnbdjitmohjavhmjobudvbsnkvszyrahpanocltwzeubgxkkthxhjgvcvygfkjctkubtjdocncmjzmxujetybdwmqutvrrulhlsbcbripctbkacwoutkrqsohiihiegqqlasykkgjjskgphieofsjlkkmvwcltgjqbpakercxypfcqqsmkowmgjglbzbidapmqoitpzwhupliynjynsdfncaosrfegquetyfhfqohxytqhjxxpskpwxegmnnppnnmgexwpkspxxjhqtyxhoqfhfyteuqgefrsoacnfdsnyjnyilpuhwzptioqmpadibzblgjgmwokmsqqcfpyxcrekapbqjgtlcwvmkkljsfoeihpgksjjgkkysalqqgeihiihosqrktuowcakbtcpirbcbslhlurrvtuqmwdbytejuxmzjmcncodjtbuktcjkfgyvcvgjhxhtkkxgbuezwtlconapharyzsvknsbvdubojmhvajhomtijdbnvkwmvtyrksbyvfpcdgrxlwpuqwicextutjyoflachmcemagxphghozkawgszqjejildejryhcyxnnwwoxmwlxsbxstrclfinqflgyxsmaqtoblfoqobiakwdlxnpkhnoxbkgjlvuhwzy"
print(len(string))
res = Solution().longestPalindrome(string)
print(res)
