class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        m = {}
        for i in s1:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1

        for i in s2:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        ans = []
        for i in m:
            if m[i] == 1:
                ans.append(i)
        return ans
        