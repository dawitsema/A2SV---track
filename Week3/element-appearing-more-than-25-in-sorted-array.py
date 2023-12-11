class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic1 = dict()
        for i in range(len(arr)):
            dic1[arr[i]] = dic1.get(arr[i], 0) + 1

        size = len(arr)
        for key, val in dic1.items():
            if val/size > 0.25:
                return key
        
        return 0
        