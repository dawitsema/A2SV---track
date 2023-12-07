class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic1 = dict()
        dic2 = dict()
        for i in range(len(matches)):
            dic1[matches[i][0]] = dic1.get(matches[i][0], 0) + 1
            dic2[matches[i][1]] = dic2.get(matches[i][1], 0) + 1
        
        winner = [key for key in dic1 if key not in dic2]
        loser = [key for key in dic2 if dic2[key] == 1]

        winner = sorted(winner)
        loser = sorted(loser)

        return [winner, loser]

        


    
        