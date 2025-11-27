class Solution:
    def myAtoi(self, s: str) -> int:

        lead_blank_trigger = False


        sign = 1
        sign_trigger = False

        num_str = "0"

        digit_trigger = False

        digit_num_possibilities = []
        for i in range(0, 10):
            digit_num_possibilities.append(str(i))

        for str_digit in s:
            print(f"digit: {str_digit}")

            #first, ignore leading zeros
            if str_digit in [" ", "0"]:
                #"   -1" -> ok
                #"  0-1" -> not ok               
                # if not lead_blank_trigger:
                #     continue
                # else:
                #     break

                if str_digit == " ":
                    #only continue if " " is at the very front
                    if (not lead_blank_trigger )and (not sign_trigger )and (not digit_trigger):
                        continue
                    else:
                        break
                else: #str_digit == "0"
                    sign_trigger = True #prevernt "    00+"
                    if not lead_blank_trigger:
                        continue
                    else:
                        num_str += str_digit

            #second, check sign
            elif str_digit in ["+", "-"]:
                lead_blank_trigger = True               
                #if already a sign
                if not sign_trigger:
                    sign_trigger = True
                    if str_digit == "-":
                        sign = -1                 
                else:
                    break
            
            elif str_digit in digit_num_possibilities:
                
                lead_blank_trigger = True
                sign_trigger = True

                num_str += str_digit
            else:
                break

        print(f"sign: {sign} num: {num_str}")

        out =  int(num_str) * sign
        if out < -2** 31:
            out = -2 ** 31
        if out > 2 ** 31 -1:
            out = 2 ** 31 -1
        return out



            

        
