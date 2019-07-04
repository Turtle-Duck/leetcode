# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = 1
        if dividend < 0:
            dividend = - dividend
            flag = flag * -1
        if divisor < 0:
            divisor = -divisor
            flag = flag * -1
        rst = 0
        while dividend >= divisor:
            dividend -= divisor
            rst += 1
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                rst += i
                temp <<= 1
                i <<= 1
        return min(max(-2147483648, rst * flag), 2147483647)
        # return rst*flag
