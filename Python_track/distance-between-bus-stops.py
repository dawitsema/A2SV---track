class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        dis = 0
        l = min(start, destination)
        r = max(start, destination)
        while l < r:
            dis += distance[l]
            l += 1

        res = min(dis, sum(distance)-dis)
        return res
        