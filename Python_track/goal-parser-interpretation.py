class Solution:
    def interpret(self, command: str) -> str:
        match = {
            "G":'G',
            "()":'o',
            "(al)":'al'
        }
        ans = ''
        temp = ''
        for ch in range(len(command)):
            temp += command[ch]
            if temp in match:
                ans += match[temp]
                temp = ""
        
        return ans

        