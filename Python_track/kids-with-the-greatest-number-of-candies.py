class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        diff = max(candies) - extraCandies
        isGreat = []*len(candies)
        for can in candies:
            if can >= diff:
                isGreat.append(True)
            else:
                isGreat.append(False)

        return isGreat
        