class Solution:
    def romanToInt(self, s: str) -> int:
        store = {
            "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000
        }

        answer = 0
        for i in range(len(s)):
            if i+1<len(s) and store[s[i]]<store[s[i+1]]:
                answer -= store[s[i]]
            else:
                answer += store[s[i]]
        return answer

        