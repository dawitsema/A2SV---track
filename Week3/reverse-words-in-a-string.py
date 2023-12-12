class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        s = " ".join(s.strip().split())
        words = s.split()

        for i in range(len(words)-1, -1, -1):
            stack.append(words[i])

        return " ".join(stack)
        