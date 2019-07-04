# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        dd = ['' for i in range(numRows)]
        count = 0
        flag = True
        for c in s:
            dd[count] += c
            if flag == True:
                count += 1
                if count == numRows - 1:
                    flag = False
            else:
                count -= 1
                if count == 0:
                    flag = True
        rst = ''
        for t in dd:
            rst += t
        return rst

