class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
      store = set()
      for i in range(len(ranges)):
        for j in range(ranges[i][0], ranges[i][1]+1):
          store.add(j)

      res = {x for x in range(left, right+1)}
      print(res)

      return store >= res

        