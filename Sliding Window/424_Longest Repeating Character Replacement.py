class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        length = 0
        isLeftPointerMoved = False

        l, r = 0, 0
        while(l <= r and r < len(s)):

            if(s[r] not in count and not isLeftPointerMoved):
                count[s[r]] = 1
            elif(s[r] in count and not isLeftPointerMoved):
                count[s[r]] += 1
            
            isLeftPointerMoved = False

            longest_len = max(count.values())
            curr_len = (r - l) + 1
            isSubStringValid =  curr_len - longest_len
            
            if (isSubStringValid <= k):
                length = max(length, curr_len)
                r += 1
                # continue
            else:
                # if left pointer moved
                if(s[l] in count): 
                    count[s[l]] -= 1
                l += 1
                isLeftPointerMoved = True


        return length
