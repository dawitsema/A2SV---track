class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        t_sum = sum(x for x in nums if x%2 == 0)
        ans = []
        for val, indx in queries:
            if nums[indx]%2 == 0:
                t_sum -= nums[indx]
            nums[indx] += val
            if nums[indx]%2 == 0:
                t_sum += nums[indx]
            ans.append(t_sum)
            
        return ans

        