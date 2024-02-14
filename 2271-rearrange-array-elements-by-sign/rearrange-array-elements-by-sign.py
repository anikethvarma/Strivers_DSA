class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        
        ans = []
        for i in range(len(nums)):
            if i%2 == 0:
                ans.append(pos[i//2])
            else:
                ans.append(neg[i//2])
        return ans