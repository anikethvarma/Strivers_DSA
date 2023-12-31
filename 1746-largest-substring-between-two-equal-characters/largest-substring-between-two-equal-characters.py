class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        uniques = list(set(s))

        ans = -1
        for char in uniques:
            temp = s.rfind(char) - s.find(char) - 1
            ans = max(ans,temp)
        return ans