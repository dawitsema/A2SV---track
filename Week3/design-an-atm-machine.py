from typing import List

class ATM:

    def __init__(self):
        self.banknote_values = [20, 50, 100, 200, 500]
        self.banknote_count = [0] * 5

    def deposit(self, banknotes_count: List[int]) -> None:
        for i, count in enumerate(banknotes_count):
            self.banknote_count[i] += count

    def withdraw(self, amount: int) -> List[int]:
        banknote_idx = 4
        withdrawal_count = [0] * 5

        while amount > 0 and banknote_idx >= 0:
            withdrawal_count[banknote_idx] = min(self.banknote_count[banknote_idx],
                                                 amount // self.banknote_values[banknote_idx])
            amount -= withdrawal_count[banknote_idx] * self.banknote_values[banknote_idx]
            banknote_idx -= 1

        if amount > 0:
            return [-1]
        else:
            for i in range(len(self.banknote_count)):
                self.banknote_count[i] -= withdrawal_count[i]
            return withdrawal_count

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotes_count)
# param_2 = obj.withdraw(amount)
