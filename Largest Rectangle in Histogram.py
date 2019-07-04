# Example:
#
# Input: [2,1,5,6,2,3]
# Output: 10


class Solution:
    def largestRectangleArea(self, heights):
        m = len(heights)
        if m < 1:
            return 0
        less_left = [0 for i in range(m)]
        less_right = [0 for i in range(m)]
        less_left[0] = -1
        less_right[-1] = m
        for i in range(m):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = less_left[p]
            less_left[i] = p
        for i in range(m):
            index = m - 1 - i
            p = index + 1
            while p < m and heights[p] >= heights[index]:
                p = less_right[p]
            less_right[index] = p

        rst = 0
        for i in range(m):
            rst = max(rst, heights[i]*(less_right[i]-less_left[i]-1))
        return rst


if __name__ == '__main__':
    a = Solution()
    rst = a.largestRectangleArea([2,1,5,6,2,3])
    print(rst)


