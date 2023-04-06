class Solution:
    def isValid(self, s: str) -> bool:
        s_arr = []
        # convert to array 
        for i in s:
            s_arr.append(i)

        stack_pop_value = ""
        key_pair_parentheses = {
            # "}": "{",
            # "]" : "[",
            # ")" : "(",
            "{": "}",
            "[" : "]",
            "(" : ")",
        }
        stack = []
        length = len(s) - 1
        for i in range(length, -1, -1):
            stack_pop_value = s_arr.pop()
            if(len(stack) < 1):
                stack.append(stack_pop_value)
                continue
          
            stack.append(stack_pop_value)

            idx_last = len(stack) - 1
            # print(key_pair_parentheses[stack[-1]], stack[-2], "<")
            if (stack[idx_last] not in key_pair_parentheses): continue
            if(key_pair_parentheses[stack[idx_last]] == stack[idx_last - 1]):
                # print(stack, "<<")
                stack.pop()
                stack.pop()
                # print(stack)
            else:
                continue
        # print(stack)
        
        return (len(stack) == 0)

    