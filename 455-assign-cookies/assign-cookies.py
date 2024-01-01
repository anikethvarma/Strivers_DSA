class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)

        pointer = 0
        ans = 0
        for i in g:
            if pointer < len(s) and i <= s[pointer]:
                ans += 1
                pointer += 1
        return ans