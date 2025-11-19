class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
          return s
        '''
        paypalishiring, num = 3
        out_arr =
           [[pay] -> zigzag = False
            [0p0] -> zigzag = True
            [ali]
            [0s0]
            [hir]
            [0i0]
            [ng0]
            [000]]
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
        # for row in out_arr:
        #     print(row)

        #change s from input string to list containing each char of input string
        temp = s
        s= []
        for i in temp:
            s.append(i)
           
        row_index = 0
        col_index = 0
       
        zigzag = False
        col_max = numRows


        while s:
            curr_char = s.pop(0)
            try:
                print(f"itr:  row: {row_index}  col: {col_index} zig:{zigzag} s:{s}\n")

                
                 #return and rmove first char from input string
                if not zigzag:
                    out_arr[row_index][col_index] = curr_char
                    col_index +=1
                    if col_index == col_max: #col_max == len(row), lead to out bound
                        col_index -=1 #-=2 ensures from len(rows) to last_index -1
                        # row_index +=1 #move down a row
                        zigzag = True
                if zigzag:                                       
                    out_arr[row_index][col_index] = curr_char
                    col_index -=1
                    row_index +=1
                    if col_index <= 0 or row_index > len(out_arr) -1:
                        zigzag = False
            except:
                print("failed below")
                print(f"itr:  row: {row_index}  col: {col_index} zig:{zigzag} \n")
        for row in out_arr:
            print(row)
        for i in range(col_max):
            for row in out_arr:
                if row[i] != 0:
                    out += row[i]
        return out
               










       

