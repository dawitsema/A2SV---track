class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)
        return sum(salary[1:-1])/(len(salary)-2)
        