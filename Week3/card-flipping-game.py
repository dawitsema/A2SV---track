class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        card_set = set(fronts + backs)
        for i in range(len(fronts)):
            if fronts[i] == backs[i] and fronts[i] in card_set:
                card_set.remove(fronts[i])
        
        if len(card_set) == 0:
            return 0
        return card_set.pop()
        
            