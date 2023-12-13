class Solution:
    def minimizedStringLength(self, s: str) -> int:
        char_dic = Counter(s)
        len_ = len(char_dic)

        return len_