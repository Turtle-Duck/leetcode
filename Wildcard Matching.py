# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:
#
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:
#
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# Example 5:
#
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dd = [[False for i in range(n+1)] for j in range(m+1)]
        dd[0][0] = True
        # for i in range(n):
        #     if p[i] == '*':
        #         dd[0][i+1] = dd[0][i-1]
        ii = 0
        while ii < n and p[ii] == '*':
            dd[0][ii + 1] = True
            ii += 1

        for j in range(m):
            for i in range(n):
                if dd[j][i]:
                    if p[i] == s[j] or p[i] == '?':
                        dd[j+1][i+1] = True
                if p[i] == '*':
                    dd[j + 1][i + 1] = dd[j][i] or dd[j + 1][i] or dd[j][i + 1]

        return dd[-1][-1]


if __name__ == '__main__':
    a = Solution()
    rst = a.isMatch("adceb", "*a*b")
    print(rst)






