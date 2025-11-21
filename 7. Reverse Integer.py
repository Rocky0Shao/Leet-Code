class Solution:
    def reverse(self, x: int) -> int:
        '''there's a wrong test case'''
    

        out = 0
        sign = 1
        if x < 0: sign = -1
        x = abs(x)

        out_list = []
        while x != 0:
            
            current_digit = x % 10
            out_list.append(current_digit)
            x = x // 10
            

        for i, j in enumerate(out_list):
            out += j * 10 ** (len(out_list) -1 - i)
        if  not -2**31 <= out <= 2**31 - 1:
            return 0
        print(out_list)
        return out * sign
