# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# Example:
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:
#
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.


class Solution:
    def minWindow(self, s, t):

        # fail in duplicate in t, such as minWindow("A", "AA")
        # d = dict()
        # for c in t:
        #     d[c] = -1
        # len_t = len(t)
        # len_s = len(s)
        #
        # small_s = -1
        # small_e = -1
        # min_len = len_s
        # for i in range(len(s)):
        #     if s[i] in d:
        #         d[s[i]] = i
        #         min_index = len_s
        #         min_c = ''
        #         for c in t:
        #             if d[c] < min_index:
        #                 min_index = d[c]
        #                 min_c = c
        #         if min_index > -1:
        #             if i - min_index < min_len:
        #                 small_s = min_index
        #                 small_e = i
        #                 min_len = small_e - small_s
        #             d[min_c] = -1
        #
        # if small_s != -1:
        #     return s[small_s:small_e+1]
        # else:
        #     return ''

        import collections
        need = collections.Counter(t)  # hash table to store char frequency
        missing = len(t)  # total number of chars we care
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s, 1):  # index j from 1
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:  # match all chars
                while i < j and need[s[i]] < 0:  # remove chars to find the real start
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1  # make sure the first appearing char satisfies need[char]>0
                missing += 1  # we missed this first char, so add missing by 1
                if end == 0 or j - i < end - start:  # update window
                    start, end = i, j
                i += 1  # update i to start+1 for next window
        return s[start:end]


if __name__ == '__main__':
    a = Solution()
    rst = a.minWindow("ADOBECODEBANC", "ABC")
    print(rst)
