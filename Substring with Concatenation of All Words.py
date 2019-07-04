# 30. Substring with Concatenation of All Words
# Hard
#
# 506
#
# 864
#
# Favorite
#
# Share
# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
#
# Example 1:
#
# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
# Example 2:
#
# Input:
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# Output: []


class Solution:
    def findSubstring(self, s, words):
        len_words = len(words)
        len_s = len(s)
        if len_words == 0 or len_s == 0:
            return []
        len_word = len(words[0])
        m = dict()
        for w in words:
            if w in m:
                m[w] += 1
            else:
                m[w] = 1
        rst = []
        for i in range(len_s - len_words * len_word + 1):
            temp_m = dict()
            flag = True
            for j in range(len_words):
                ttt = s[i + j * len_word:i + (j + 1) * len_word]
                if ttt in m:
                    if ttt not in temp_m:
                        temp_m[ttt] = 1
                    else:
                        temp_m[ttt] += 1
                    if temp_m[ttt] > m[ttt]:
                        flag = False
                        break
                else:
                    flag = False
                    break
                # if ttt in temp_m:
                #     if temp_m[ttt] > 0:
                #         temp_m[ttt] -= 1
                #     else:
                #         flag = False
                #         break
                # else:
                #     flag = False
                #     break
            if flag:
                rst.append(i)

        return rst


if __name__ == '__main__':
    a = Solution()
    rst = a.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])
    print(rst)
