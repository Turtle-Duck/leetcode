class Solution_old:

    def s(self, nums, l, r, is_right, target):
        if not is_right:
            llll = r
            while l < r and target == nums[r]:
                llll = r
                if target == nums[l]:
                    llll = l
                    break
                mid_i = int((l + r) / 2)
                if nums[mid_i] < target:
                    l = mid_i + 1
                else:
                    llll = mid_i
                    r = mid_i - 1
            return llll
        else:
            rrrr = l
            while l < r and target == nums[l]:
                rrrr = l
                if target == nums[r]:
                    rrrr = r
                    break
                mid_i = int((l + r) / 2)
                if nums[mid_i] > target:
                    r = mid_i - 1
                else:
                    rrrr = mid_i
                    l = mid_i + 1
            return rrrr

    def searchRange(self, nums, target):
        l = 0
        r = len(nums)
        if r == 0:
            return [-1, -1]
        elif r == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        r = r - 1
        p = -1
        l_rst = -1
        r_rst = -1
        while l < r:
            if nums[l] == target:
                l_rst = l
            if nums[r] == target:
                r_rst = r
            mid_i = int((l + r) / 2)
            if nums[mid_i] < target:
                l = mid_i + 1
            elif nums[mid_i] > target:
                r = mid_i - 1
            else:
                p = mid_i
            if l_rst != -1 or r_rst != -1 or p != -1:
                break

        if l_rst != -1 and r_rst != -1:
            return [l_rst, r_rst]
        elif l_rst != -1 and r_rst == -1:
            if p == -1:
                return [l_rst, self.s(nums, l_rst, r, 1, target)]
            else:
                return [l_rst, self.s(nums, p, r, 1, target)]
        elif l_rst == -1 and r_rst != -1:
            if p == -1:
                return [self.s(nums, l, r_rst, 0, target), r_rst]
            else:
                return [self.s(nums, l, p, 0, target), r_rst]
        else:
            if p == -1:
                return [-1, -1]
            else:
                return [self.s(nums, l, p, 0, target), self.s(nums, p, r, 1, target)]


class Solution:

    def s(self, nums, target, left):
        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r) // 2
            if (nums[mid] == target and left) or nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l

    def searchRange(self, nums, target):
        l_i = self.s(nums, target, True)
        if l_i == len(nums) or nums[l_i] != target:
            return [-1, -1]
        return [l_i, self.s(nums, target, False) - 1]


if __name__ == '__main__':
    a = Solution()
    rst = a.searchRange([0,1,2,3,3,4,4,5,5,6,6,7,7,7,9,9,11,11,11,12,12,12,12], 12)
    print(rst)
