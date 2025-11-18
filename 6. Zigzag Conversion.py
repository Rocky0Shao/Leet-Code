class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        paypalishiring, num = 3
        out_arr = 
           [[pay] -> zigzag = False
            [0p0] -> zigzag = True
            [ali]
            [0s0]
            [hir]
            [0i0]
            [ng0]]
        out = ""
        for col in out_arr:
            for char in col:
                if char != 0:
                    out += char
        return out
        '''

        #this below initlize out_arr to all zeros
        out = ""
        out_arr = []
        #first initialize out_arr to all 0s
        for i in range(0,(numRows -1) * math.floor(len(s)//numRows + 0.5)):
            temp_row = []
            for j in range(numRows):
                temp_row.append(0)
            out_arr.append(temp_row)
        
        row_index = 0
        col_index = 0
        s_index = 0
        zigzag = False
        col_max = numRows
        temp = s
        s= []
        for i in temp:
            s.append(i)
        while s:
            print(f"row: {row_index}, col: {col_index}")
            curr_char = s.pop(s_index) #return and rmove first char from input string
            if not zigzag:
                out_arr[row_index][col_index] = curr_char
                col_index +=1
                if col_index == col_max: #col_max == 3, lead to out bound
                    col_index -=1
                    zigzag = True
            if zigzag:
                col_index -=1
                row_index +=1
                out_arr[row_index][col_index] = curr_char
                if col_index == 0:
                    zigzag = False
        for row in out_arr:
            print(row)
                





        
