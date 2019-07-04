# # The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
# #
# # Example:
# #
# # Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# # Output: 6
#
#
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#


class Solution:

    def sumsum(self, height, from_left, end_index):
        if from_left:
            old = height[0]
            old_max = height[0]
            index_list = list(range(1, end_index))
        else:
            old = height[-1]
            old_max = height[-1]
            index_list = list(range(end_index, len(height) - 1))
            index_list.reverse()

        rst = 0
        left = False
        for i in index_list:
            if not left:
                if height[i] >= old:
                    old_max = height[i]
                else:
                    left = True
                    rst += (old_max - height[i])
            else:
                if height[i] >= old_max:
                    left = False
                    old_max = height[i]
                else:
                    rst += (old_max - height[i])
            old = height[i]
        return rst

    def trap(self, height):
        if len(height) < 3:
            return 0
        max_index = list()
        max_h = -1e30
        for i in range(len(height)):
            if height[i] > max_h:
                max_h = height[i]
        for i in range(len(height)):
            if height[i] == max_h:
                max_index.append(i)
        rst = 0
        rst += self.sumsum(height, True, max_index[0])
        rst += self.sumsum(height, False, max_index[-1])
        for i in range(max_index[0], max_index[-1]):
            rst += (height[max_index[0]] - height[i])
        return rst


if __name__ == '__main__':
    a = Solution()
    rst = a.trap([2,0,2])
    print(rst)
