class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        arr = []
        if num%3 != 0:
            return []
        else:
            arr.append(num//3 - 1)
            arr.append(num//3)
            arr.append(num//3 + 1)
        total = 0
        for ar in arr:
            total += ar
        if total == num:
            return arr
        else:
            return []


        