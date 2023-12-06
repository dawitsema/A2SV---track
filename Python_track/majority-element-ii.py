class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        set1 = set(nums)
        k = len(nums)//3
        ans = []
        for val in set1:
            m = nums.count(val)
            if m > k:
                ans.append(val)

        return ans

        