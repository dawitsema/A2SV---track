class Solution:
    def fillCups(self, amount: List[int]) -> int:
        max_amount = max(amount)
        sum_2 = sum(amount)-max_amount
        if sum_2 > max_amount:
            diff = sum_2 - max_amount
            diff = ceil(diff/2)
        else:
            diff = 0

        return max_amount + diff



        