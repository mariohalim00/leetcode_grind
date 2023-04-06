class Solution:
    # define local variable to store basic roman numeral and it's value
    def romanToInt(self, s: str) -> int:
        dict_roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        res = 0 # result variable
        skip_flag = False # for skipping iteration

        for index, i in enumerate(s):
            
            # if skip_flag is true: set it to false, subtract current letter from the letter before the current letter 
            if(skip_flag):
                skip_flag = False
                res += (dict_roman[i] - dict_roman[s[index - 1]])
                continue               
            # get next_char with edge case protection   
            if(index != len(s)-1 ): 
                next_char = s[index + 1]
            else:
                next_char = ""
            
            # while edge case condition is not met, see if it matches the special properties of roman numeral
            # e.g I->V ==> 4 
            if((next_char == 'V' or next_char == 'X') and i == 'I' ):
                skip_flag = True 
                continue
            elif((next_char == 'L' or next_char == 'C') and i == 'X' ):
                skip_flag = True
                continue
            elif((next_char == 'D' or next_char == 'M') and i == 'C' ):
                skip_flag = True
                continue
            else:
                # if no matches, add the letter itself
                res += dict_roman[i]
        return res