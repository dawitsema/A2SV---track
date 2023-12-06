class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        least = []
        great = []
        equ = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                least.append(nums[i])
            elif nums[i] == pivot:
                equ.append(nums[i])
            else:
                great.append(nums[i])
       
        equ.extend(great)
        least.extend(equ)
        return least