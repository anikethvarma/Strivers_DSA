class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        f = 0
        
        for i in range(31, -1, -1):
            if ((n >> i) & 1) == 1:
                if f == 0:
                    ans = ans + ((1 << (i + 1))) - 1
                    f = 1
                else:
                    ans = ans - ((1 << (i + 1)) - 1)
                    f = 0
        
        return ans


