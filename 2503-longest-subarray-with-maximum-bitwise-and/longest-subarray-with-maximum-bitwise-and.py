class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = nums[0]
        max_len = 1
        current_len = 1
        for i in range(1, len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
                max_len = 1
                current_len = 1
            elif nums[i] == max_val:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 0
        return max_len

