class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split()
        if(s):
            return len(s[-1])
        return 0