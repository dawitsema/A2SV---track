class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            if words[i][0].lower() in "qwertyuiop":
                for ch in words[i]:
                    if ch.lower() not in "qwertyuiop":
                        break;
                else:
                    ans.append(words[i])


            elif words[i][0].lower() in "asdfghjkl":
                for ch in words[i]:
                    if ch.lower() not in "asdfghjkl":
                        break;
                else:
                    ans.append(words[i])

            elif words[i][0].lower() in "zxcvbnm":
                for ch in words[i]:
                    if ch.lower() not in "zxcvbnm":
                        break;
                else:
                    ans.append(words[i])

        return ans
