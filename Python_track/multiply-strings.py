class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if 1 <= len(num1) and len(num2) <= 200:
            store = int(num1)*int(num2)
            return str(store)
        