#
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"


class Solution_slowdp:
    def longestValidParentheses(self, s):
        s_len = len(s)
        if s_len < 2:
            return 0
        m = [[False for i in range(s_len)] for j in range(s_len)]

        rst = 0
        if_first = True

        for i in range(s_len - 1):
            if s[i:i + 2] == '()':
                m[i][i + 1] = True
                if if_first:
                    rst = 2
                    if_first = False

        for t in range(int(s_len / 2) - 1):
            temp_rst = 3 + 2 * t + 1
            for i in range(s_len - 3 - 2 * t):
                j = i + 3 + 2 * t
                if m[i+1][j-1] and s[i] == '(' and s[j] == ')':
                    m[i][j] = True
                    rst = temp_rst
                else:
                    for q in range(1, 3 + 2*t, 2):
                        if m[i][i+q] and m[i+q+1][j]:
                            m[i][j] = True
                            rst = temp_rst
                            break
        # rst = 0
        # for t in range(int(s_len / 2)):
        #     for i in range(2 * t + 1):
        #         if m[i][s_len-1-i]:
        #             rst = s_len - i - 1

        return rst


class Solution:
    def longestValidParentheses(self, s):
        s_len = len(s)
        if s_len < 2:
            return 0
        m = [0 for i in range(s_len)]

        for i in range(1, s_len):
            if s[i] == ')':
                if s[i-1] == '(':
                    m[i] = m[i-2] + 2
                else:
                    if i-m[i-1]-1 >= 0 and s[i-m[i-1]-1] == '(':
                        m[i] = m[i - 1] + 2 + m[i-m[i-1]-2]

        return max(m)


if __name__ == '__main__':
    a = Solution()
    rst = a.longestValidParentheses("(()))())(")
    print(rst)