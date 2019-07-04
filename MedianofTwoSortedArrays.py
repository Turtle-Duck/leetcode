# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m,  nums2, nums1
        start = 0
        end = m
        while start <= end:
            i = int((start + end) / 2)
            j = int((m + n) / 2) - i
            if i < m and j > 0 and nums1[i] < nums2[j-1]:
                start = i + 1
            elif i > 0 and j < n and nums2[j] < nums1[i-1]:
                end = i - 1
            else:
                if i == m:
                    min_r = nums2[j]
                elif j == n:
                    min_r = nums1[0]
                else:
                    min_r = min(nums1[i], nums2[j])
                if (m+n) % 2 == 1:
                    return min_r

                if i == 0:
                    max_l = nums2[j-1]
                elif j == 0:
                    max_l = nums1[i-1]
                else:
                    max_l = max(nums1[i-1], nums2[j-1])
                return 0.5*(min_r + max_l)
        # if m == 0:
        #     if n == 1:
        #         return nums2[0]
        #     if n % 2 == 1:
        #         return nums2[int(n / 2)]
        #     else:
        #         return 0.5*(nums2[int(n / 2)] + nums2[int(n / 2) - 1])
        # if m == 1:
        #
        #
        # if (m + n) % 2 == 0:
        #     flag = 0
        # else:
        #     flag = 1
        # start = 0
        # end = m - 1
        # while start < end:
        #     mm = int((start + end) / 2)
        #     nn = int((m + n - 2 * mm) / 2) - 2
        #     if nums1[mm] <= nums2[nn+1] and nums2[nn] <= nums1[mm+1]:
        #         if flag:
        #             return min(nums1[mm+1], nums2[nn+1])
        #         else:
        #             return 0.5 * (min(nums1[mm+1], nums2[nn+1]) + max(nums1[mm], nums2[nn]))
        #     else:
        #         if nums1[mm] > nums2[nn+1]:
        #             end = mm
        #         else:
        #             start = mm


if __name__ == '__main__':
    a = Solution()
    rst = a.findMedianSortedArrays([3], [2, 4, 7])
    print(rst)





