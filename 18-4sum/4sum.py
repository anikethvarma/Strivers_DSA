class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                pointer_1 = j + 1
                pointer_2 = n-1
                remaining = target - nums[i] - nums[j]
                while(pointer_1 < pointer_2):
                    if nums[pointer_1] + nums[pointer_2] == remaining and [nums[i],nums[j],nums[pointer_1],nums[pointer_2]] not in ans:
                        ans.append([nums[i],nums[j],nums[pointer_1],nums[pointer_2]])
                        pointer_1 += 1
                    elif nums[pointer_1] + nums[pointer_2] > remaining:
                        pointer_2 -= 1
                    else:
                        pointer_1 += 1
                    


        return ans
        