class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        n = len(max(words, key=len))
        ans = []
        for i in range(n):
            temp = []
            for word in words:
                temp.append(word[i] if i < len(word) else " ")
            ans.append("".join(temp).rstrip())
        
        return ans

        