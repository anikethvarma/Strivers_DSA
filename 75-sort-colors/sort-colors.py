class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for iter in range(len(nums)):
            flag = 0
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    temp = nums[i] 
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
                    flag = 1
            if flag == 0:
                return
        