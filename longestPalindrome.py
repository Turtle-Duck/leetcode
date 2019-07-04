# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        if n == 1 or n == 0:
            return s
        dd = [[False for j in range(n)] for i in range(n)]
        for i in range(n):
            dd[i][i] = True

        start = 0
        end = 0
        found = False
        for i in range(n-1):
            if s[i] == s[i+1]:
                dd[i][i+1] = True
                if not found:
                    start = i
                    end = i + 1
                    found = True

        for i in range(2, n):
            found = False
            for j in range(n-i):
                if dd[j+1][j+i-1] and s[j] == s[j+i]:
                    dd[j][j + i] = True
                    if not found:
                        start = j
                        end = j + i
                        found = True

        return s[start:end+1]

    def longestPalindrome_2(self, s: str) -> str:
    # def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]


if __name__ == '__main__':
    a = Solution()
    rst = a.longestPalindrome("babad")
    print(rst)




