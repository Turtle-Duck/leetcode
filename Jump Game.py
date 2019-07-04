# 55. Jump Game
# # Medium
# #
# # 1965
# #
# # 201
# #
# # Favorite
# #
# # Share
# # Given an array of non-negative integers, you are initially positioned at the first index of the array.
# #
# # Each element in the array represents your maximum jump length at that position.
# #
# # Determine if you are able to reach the last index.
# #
# # Example 1:
# #
# # Input: [2,3,1,1,4]
# # Output: true
# # Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# # Example 2:
# #
# # Input: [3,2,1,0,4]
# # Output: false
# # Explanation: You will always arrive at index 3 no matter what. Its maximum
# #              jump length is 0, which makes it impossible to reach the last index.


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = len(nums)
        if m < 2:
            return True
        # rst = [False for i in range(m)]
        # rst[-1] = True
        last_point = m - 1
        for i in range(m - 1):
            index = m - 2 - i
            long = nums[index]
            if index + long >= last_point:
                last_point = index
            # end = min(index+long+1, m)
            # # print(long, end)
            # for j in range(index, end):
            #     temp_index = index+end-1-j
            #     if rst[temp_index]:
            #         rst[index] = True
            #         break
            # # print(rst)
        if last_point == 0:
            return True
        else:
            return False
