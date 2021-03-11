
INT_MIN = -(2**31)
INT_MAX = 2**31 -1

class Solution:


    def __init__(self):
        self.state_table = {
            # state_name => input character [+/-, number, white space, other]
            "start": ["signed", "number", "start", "end"], # next state
            "end": ["end", "end", "end", "end"],
            "signed": ["end", "number", "end", "end"],
            "number": ["end", "number", "end", "end"]
        }

    def myAtoi(self, s: str) -> int:
        ans = 0
        sign = 1
        state = "start"

        for c in s:
            index = self.__charType(c)
            state = self.state_table[state][index] # next state
            if state == "number":
                ans = ans*10 + int(c)
            elif state == "end":
                break
            elif state == "signed":
                sign = -1 if c == "-" else 1

        if sign == -1:
            return max(-ans, INT_MIN)
        else:
            return min(ans, INT_MAX)

    def __charType(self, c):
        if(c == "+" or c == "-"):
            return 0
        elif (c.isspace()):
            return 2
        elif (c.isdigit()):
            return 1
        else:
            return 3




test_str = ["42",
"   -42",
"4193 with words",
"words and 987",
"-+91283472332a"
"-91283472332"]
res = Solution().myAtoi(test_str[4])
print("result", res)