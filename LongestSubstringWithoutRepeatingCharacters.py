class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_str = list()
        max_len = 0
        # record = [0 for i in range(26)]
        record = {}
        # ord('a') 97
        for c in s:
            # if record[ord(c)-97] != 0:
            if c in record:
                while max_str[0] != c:
                    # record[max_str[0]] = 0
                    record.pop(max_str[0])
                    del max_str[0]
                del max_str[0]
            record[c] = 1
            max_str.append(c)
            if len(max_str) > max_len:
                max_len = len(max_str)
        return max_len


if __name__ == '__main__':
    a = Solution()
    a.lengthOfLongestSubstring()
