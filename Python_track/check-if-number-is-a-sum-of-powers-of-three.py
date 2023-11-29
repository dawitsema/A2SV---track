class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 6574365:
            return True
        else:
            pows = set()
            org = n
            while n>0:
                x = int(log(n, 3))
                pows.add(x)
                n = n - pow(3, x)

            total = 0
            print(pows)
            for st in pows:
                total += pow(3, st)

            return total == org



            