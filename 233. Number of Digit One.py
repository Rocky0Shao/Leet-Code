class Solution:
    def countDigitOne(self, n: int) -> int:
        '''
        0~9: 1
        10~19: 10
        20~29: 1
        30~39: 1


        '''
        out = 0
        for i in range (0, n+1):
            str_i = str(i)
            for char in str_i:
                if char == "1":
                    out +=1
        return out
