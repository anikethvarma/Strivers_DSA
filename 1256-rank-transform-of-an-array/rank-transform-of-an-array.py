class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = arr.copy()
        temp.sort()

        m = dict()
        r = 1
        for i in temp:
            if i not in m:
                m[i] = r 
                r += 1
        
        for i in range(len(arr)):
            arr[i] = m[arr[i]]
        return arr