class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        output = [[1], [1, 1]] 
        for j in range(2, numRows): 
            new_row = [1]  
            old_row = output[j - 1]  
            for i in range(1, j):  
                new_row.append(old_row[i - 1] + old_row[i])
            new_row.append(1)  
            output.append(new_row) 

        return output
