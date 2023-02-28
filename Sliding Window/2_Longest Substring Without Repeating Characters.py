class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        str_res = "" 
        for i in range(len(s)):
            curr_longest_str = []
            # odd
            l, r = i, i+1
            curr_longest_str.append(s[l])
            while(r < len(s) and s[r] not in curr_longest_str):
                curr_longest_str.append(s[r])
                r+=1
            
            length = max(length, len(curr_longest_str))

            

        print(length, str_res)
        return length