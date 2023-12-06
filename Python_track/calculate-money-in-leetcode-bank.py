class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        for week in range(1, ceil(n / 7) + 1):
            for day in range(1, 8):
                if (week - 1) * 7 + day <= n:
                    total += (week - 1) + day

        return total

        