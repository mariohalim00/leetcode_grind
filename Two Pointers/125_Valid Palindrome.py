class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove space and other delimiter
        formatted_str = s.lower().translate(str.maketrans("", "", string.punctuation))
        temp = formatted_str.split(" ")
        formatted_str = "".join(temp)

        # start checking using two pointer
        i, j = 0, len(formatted_str) - 1
        while(j > i):
            if(formatted_str[i] != formatted_str[j]): 
                return False
            i += 1
            j -= 1
        return True

# OLD SOLUTIONS (MAY 02 2022)
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         #remove space and other delimiter
#         formatted_str = s.lower().translate(str.maketrans("", "", string.punctuation))
#         temp = formatted_str.split(" ")
#         formatted_str = "".join(temp)
        
#        # using sliding window
#         i = 0 
#         j = len(formatted_str) - 1
        
#         if(j == -1): return True
        
#         while(i <= j):
#             if(i == j):
#                 return True
            
#             if(formatted_str[i] == formatted_str[j]):
#                 if(j - i == 1):
#                     return True
#                 i+=1
#                 j-=1
#                 continue
#             else:
#                 return False
        # #reverse
        # reversed_str = formatted_str[::-1]
        # #compare
        # if reversed_str == formatted_str:
        #     return True
        # else:
        #     return False
        