class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        count = 0
        for i in range(len(s)):
            if count < len(spaces) and spaces[count] == i:
                ans.append(" ")
                count += 1
                ans.append(s[i])
            else:
                ans.append(s[i])
        return "".join(ans)