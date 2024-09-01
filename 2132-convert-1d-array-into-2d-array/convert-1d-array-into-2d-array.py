class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []

        res = []
        for i in range(m):
            res.append(original[n*i:(n*i)+n])
        return res