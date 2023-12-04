class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        k = abs(target[0])+abs(target[1])
        flag = True
        for ghost in ghosts:
            tmp = abs(target[0]-ghost[0]) + abs(target[1]-ghost[1])
            if tmp <= k:
                flag = False
                break

        return flag

        

        