class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        output = []
        letters = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        base = [] 
        #for number in input digit, base store the list of paring letter of each number
        for letter in digits:
            base.append(letters[letter])
        possibilities=1
        for i in base:
            possibilities *= len(i)

        positions = []
        for i in range(len(digits)):
            positions.append(0)

        
        while True:
            single_output =""
            for i in range(len(digits)):
                single_output += base[i][positions[i]]
            output.append(single_output)
            if len(output) == possibilities:
                break
            #start manilpulating elements in the list positions
            positions[-1]+=1
            for i in range(-1,-1*len(digits)-1,-1):
                if positions[i] == len(base[i]):
                    positions[i] = 0
                    positions[i-1]+=1


        return output
