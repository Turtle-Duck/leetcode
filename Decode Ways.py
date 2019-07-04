# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


class Solution:
    def numDecodings(self, s: str) -> int:
        m = len(s)
        if m == 0 or s[0] == '0':
            return 0
        if m == 1:
            if s >= '1' and s <= '9':
                return 1
            else:
                return 0
        record = [0 for i in range(m)]

        #         if s[-1] >= '1':
        #             record[-1] = 1
        #         else:
        #             record[-1] = -1
        #         temp = int(s[-2:])
        #         if temp == 0:
        #             record[-2] = 0
        #         elif temp
        #         if int(s[-2:]) > 26:
        #             record[-2] = 1
        #         else:
        #             record[-2] = 2

        temp = int(s[-2:])
        if temp == 0:
            return 0
        elif temp < 10:
            record[-1] = 1
            record[-2] = 0
        elif temp == 10:
            record[-1] = 0
            record[-2] = 1
        elif temp < 20:
            record[-1] = 1
            record[-2] = 2
        elif temp == 20:
            record[-1] = -1
            record[-2] = 1
        elif temp <= 26:
            record[-1] = 1
            record[-2] = 2
        else:
            record[-1] = 1
            record[-2] = 1
        if s[-1] == '0' and s[-2] > '2':
            return 0

        for i in range(m - 2):
            index = m - i - 3
            if s[index + 1] == '0' and (s[index] > '2' or s[index] == '0'):
                return 0
            if int(s[index:index + 2]) > 26:
                record[index] = record[index + 1]
            else:
                record[index] = record[index + 1] + record[index + 2]
            if s[index + 1] == '0':
                record[index] = record[index + 2]
            elif s[index + 2] == '0':
                record[index] = record[index + 1]
        return record[0]

    def numDecodings_1(self, s):
        v, w, p = 0, int(s > ''), ''
        for d in s:
            v, w, p = w, (d > '0') * w + (9 < int(p + d) < 27) * v, d
        return w


if __name__ == '__main__':
    a = Solution()
    rst = a.numDecodings_1('000')
    print(rst)


