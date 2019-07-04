#
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
#
# Example 1:
#
# Input: [1,3,4,2,2]
# Output: 2
# Example 2:
#
# Input: [3,1,3,4,2]
# Output: 3
# Note:
#
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.


class Solution:
    # # change the array
    # def findDuplicate(self, nums):
    #     m = len(nums)
    #     rst = 0
    #     for i in range(m):
    #         if nums[i] != i + 1:
    #             new_index = nums[i] - 1
    #             while nums[new_index] != new_index + 1:
    #                 temp = nums[new_index] - 1
    #                 nums[new_index] = new_index + 1
    #                 if new_index == i:
    #                     break
    #                 new_index = temp
    #             if new_index != i:
    #                 rst = nums[new_index]
    #                 break
    #     return rst

    # not change the array
    def findDuplicate(self, nums):
        m = len(nums)
        rst = 0
        for i in range(m):
            if nums[i] != i + 1:
                new_index = nums[i] - 1
                while True:
                    if nums[new_index] == new_index + 1:
                        break
                    temp = nums[new_index] - 1
                    # nums[new_index] = new_index + 1
                    if new_index == i:
                        break
                    new_index = temp
                if new_index != i:
                    rst = nums[new_index]
                    break
        return rst


if __name__ == '__main__':
    a = Solution()
    rst = a.findDuplicate([1,3,4,2,2])
    print(rst)
