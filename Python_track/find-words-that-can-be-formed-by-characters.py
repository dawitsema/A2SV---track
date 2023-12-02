class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        store = chars
        count = 0
        for word in words:
            chars = store
            i = 0
            while i<len(word):
                if word[i] in chars:
                    chars = chars.replace(word[i], "", 1)
                    i += 1
                else:
                    break
            else:
                count += len(word)
        
        return count

        

        