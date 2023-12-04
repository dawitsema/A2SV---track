class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newarr = []
        n = len(nums)
        for i in range(2*len(nums)):
            if i < len(nums):
                newarr.append(nums[i])
            else:
                newarr.append(nums[i-n])

        return newarr