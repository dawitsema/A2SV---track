class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        m = ''
        d = ''
        for word in word1:
            m += word
        for word in word2:
            d += word
        return m == d