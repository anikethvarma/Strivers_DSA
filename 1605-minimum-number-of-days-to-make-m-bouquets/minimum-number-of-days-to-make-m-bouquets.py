class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def isPossible(bloomDay, mid, k, m):
            boq = 0
            count = 0
            for i in bloomDay:
                if i <= mid:
                    count += 1
                else:
                    count = 0
                if count == k:
                    boq += 1
                    count = 0
                if boq >= m:
                    return True
            return False


        low = 1
        high = 2**31
        ans = -1

        while(low <= high):
            mid = low + (high - low)//2

            if isPossible(bloomDay,mid,k,m):
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1

        return ans
        


