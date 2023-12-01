class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i
        
        for i in range(len(words)-1):
            tmp1 = words[i]
            tmp2 = words[i+1]
            n = min(len(tmp1), len(tmp2))
            for j in range(n):
                if dic[tmp1[j]] < dic[tmp2[j]]:
                    break
                elif dic[tmp1[j]] == dic[tmp2[j]]:
                    continue
                else:
                    return False
            else:
                if len(tmp1) > len(tmp2):
                    return False


        return True
