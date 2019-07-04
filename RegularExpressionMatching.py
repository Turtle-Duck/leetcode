# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
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
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
# Example 5:
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false


class Solution:
    def isMatch(self, s, p):
        # rst = True
        # i = 0
        # j = 0
        # m = len(s)
        # n = len(p)
        # have_all = False
        # if '.*' in p:
        #     have_all = True
        # if not have_all:
        #     while j < n:
        #         p_chr = p[j]
        #         if j < n - 1 and p[j+1] == '*':
        #             j += 2
        #             if p_chr == '.':
        #                 while i < m:
        #                     i += 1
        #             else:
        #                 while i < m and s[i] == p_chr:
        #                     i += 1
        #         else:
        #             j += 1
        #             if i == m:
        #                 rst = False
        #                 break
        #             if s[i] == p_chr or p_chr == '.':
        #                 i += 1
        #             else:
        #                 break
        #     if i < m or j < n:
        #         rst = False
        # else:
        #     while j < n:
        #         p_chr = p[j]
        #         if j < n - 1 and p[j + 1] == '*':
        # return rst
        m = len(s)
        n = len(p)
        dd = [[False for i in range(n+1)] for j in range(m+1)]
        dd[0][0] = True
        for i in range(n):
            if p[i] == '*':
                dd[0][i+1] = dd[0][i-1]

        for j in range(m):
            for i in range(n):
                if dd[j][i]:
                    if p[i] == s[j] or p[i] == '.':
                        dd[j+1][i+1] = True
                if p[i] == '*':
                    if s[j] != p[i-1] and p[i-1] != '.':
                        dd[j + 1][i + 1] = dd[j + 1][i - 1]
                        # ba*
                        # bc
                    else:
                        dd[j + 1][i + 1] = dd[j + 1][i - 1] or dd[j + 1][i] or dd[j][i + 1]
                        #                  ba*                 ba*             ba*
                        #                  b                   ba              baaaaa

        return dd[-1][-1]


if __name__ == '__main__':
    a = Solution()
    rst = a.isMatch("mississippi", "mis*is*ip*.")
    print(rst)



