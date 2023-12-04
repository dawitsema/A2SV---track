class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        forward = 0
        backward = 0
        st = capacity
        for i, pl in enumerate(plants):
            if capacity >= pl:
                forward += 1
            elif capacity < pl:
                capacity = st
                backward += i
                forward += i+1
            
            capacity -= pl
        return forward + backward



        