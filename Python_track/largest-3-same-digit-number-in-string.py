class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = 0
        flag = False
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                flag = True
                ans = max(int(num[i:i+3]), ans)
        if flag:
            if ans == 0:
                return "000"
            else:
                return str(ans)
        else:
            return ""
        

        

        