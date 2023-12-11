class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        nums = list(nums)
        nums = sorted(nums)
        print(nums)
        ans = 1
        count = 1
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                 count += 1
                 ans = max(ans, count)
            else:
                count = 1
        if nums:
            return ans
        else:
            return 0

        