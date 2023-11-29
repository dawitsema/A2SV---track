class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        strs = sorted(strs)
        firstWord = strs[0]
        lastWord = strs[-1]
        for i in range(min(len(firstWord), len(lastWord))):
            if (firstWord[i] != lastWord[i]):
                return result
            result += firstWord[i]
        return result 

        