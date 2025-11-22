'''
def triangulate(list)"
    if len(list) == 3: 
        return base_case_comput
    //else: start recurse

    start_index, start_value = find_start(list) //choose the min in list to start
    next_index, next_value = find_next(list, start_index)
        //choose the next min (not adjacent from start)

    sublist1, sublist2 = break_list(list)
        //below 2 lines, start, next, 0, end are all indexes
        //however, sublist1 and sublist2 contains values (for future recursion)
        //sublist1: start ~ next , both ends inclusive
        //sublist2: 0~start (0 & start both inclusive) + next ~ end-> (next & end both inclusive) 
    return triangulate{sublist1} + triangulate(sublist2)    
'''



def find_start(values: List[int]) -> tuple[int]:
    start_index = 200
    start_value = 200
    for i,j in enumerate(values):
        if j < start_value:
            start_index = i
            start_value = j    
    # print(f"start_index: {start_index}  start_value: {start_value}")        
    return (start_index, start_value)

def find_next(values: List[int], current_index: int) -> tuple[int]:
    prev_index = current_index -1
    next_index = current_index + 1
    if prev_index == -1:
        prev_index = len(values)-1
    if next_index == len(values):
        next_index = 0
    adjacents = [prev_index, current_index, next_index]
    # print(f"adjacents: {adjacents}")
    min_index = 200
    min_value = 200
    for i,j in enumerate(values):
        if i in adjacents:
            # print(f"i: {i} passed")
            pass        
        else:
            if j < min_value:
                min_index = i
                min_value = j
    # print(f"next_index: {min_index}  next_value: {min_value}")
    return (min_index, min_value)

def break_list(values: List[int], start_index: int, next_index: int) -> Tuple[List[int], List[int]]:
    sublist1 = values[start_index : next_index + 1]
    sublist2 = values[0 : start_index + 1] + values [next_index : len(values)]
    print(f"sublist1: {sublist1}")
    print(f"sublist2: {sublist2}")

    return (sublist1, sublist2)

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        if len(values) == 3:
            print(f"trig: {values}")
            return values[0] * values[1] * values[2]
        
        start_index, start_value = find_start(values)
        next_index, next_value = find_next(values, start_index)
        
        
        sublist1, sublist2 = break_list(values, start_index, next_index)
        print("end one function \n")
        return self.minScoreTriangulation(sublist1) + self.minScoreTriangulation(sublist2)

        
        
