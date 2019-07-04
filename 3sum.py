def twosum(rst: set, number, nums):
    a = dict()
    for i in nums:
        # a[i]
        if number - i in a:
            temp = [-number, i, number - i]
            rst.add(tuple(sorted(temp)))
        a[i] = 1


class Solution:

    #     def threeSum(self, nums: List[int]) -> List[List[int]]:
    #         nums = sorted(nums)
    #         rst = list()
    #         for i in range(len(nums) - 2):
    #             if nums[i]>0: break #[7]
    #             if i>0 and nums[i]==nums[i-1]: continue #[1]

    #             l = i + 1
    #             r = len(nums) - 1
    #             while l < r:
    #                 total = nums[i] + nums[l] + nums[r]
    #                 if total < 0:  # [3]
    #                     l += 1
    #                 elif total > 0:  # [4]
    #                     r -= 1
    #                 else:  # [5]
    #                     rst.append([nums[i], nums[l], nums[r]])
    #                     while l < r and nums[l] == nums[l + 1]:  # [6]
    #                         l += 1
    #                     while l < r and nums[r] == nums[r - 1]:  # [6]
    #                         r -= 1
    #                     l += 1
    #                     r -= 1
    #         return rst

    def threeSum(self, nums):
        # nums = sorte(nums)
        # nums = nums[:2] + list(set(nums[2:]))
        if len(nums) > 3:
            nums = sorted(nums)
            new_nums = nums[:3]
            for i in range(3, len(nums)):
                if nums[i] == nums[i - 1] and nums[i] == nums[i - 2] and nums[i] == nums[i - 3]:
                    pass
                else:
                    new_nums.append(nums[i])
            nums = new_nums

        rst = set()
        for i in range(len(nums) - 2):
            twosum(rst, -nums[i], nums[i + 1:])
        real_rst = list()
        for r in rst:
            real_rst.append(list(r))
        print(real_rst)
        return real_rst


class Solution_best(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length-2): #[8]
            if nums[i]>0: break #[7]
            if i>0 and nums[i]==nums[i-1]: continue #[1]

            l, r = i+1, length-1 #[2]
            while l<r:
                total = nums[i]+nums[l]+nums[r]

                if total<0: #[3]
                    l+=1
                elif total>0: #[4]
                    r-=1
                else: #[5]
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]: #[6]
                        l+=1
                    while l<r and nums[r]==nums[r-1]: #[6]
                        r-=1
                    l+=1
                    r-=1
        return res
