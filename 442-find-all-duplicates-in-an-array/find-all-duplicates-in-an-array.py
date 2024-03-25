class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            x = abs(x)
            if nums[x-1] < 0:
                ans.append(x)
            nums[x-1] *= -1
        return ans