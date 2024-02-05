class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.rindex(s[i]) == i and s.index(s[i]) == i:
                return i
        return -1