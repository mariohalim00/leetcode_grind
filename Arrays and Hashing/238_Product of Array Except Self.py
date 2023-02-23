class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret_val = [1 for i in nums]
        i = 0
        while (i < len(nums)):
            if(i - 1 < 0):
                i+=1
                continue 
            else:
                ret_val[i] = ret_val[i - 1] * nums[i - 1]
                i += 1

        postfix = 1
        while(i >= 0):
            if(i == len(nums)):
                i-=1
                continue
            else:
                ret_val[i] = ret_val[i] * postfix
                postfix *= nums[i]
                i-=1
                


            
        return ret_val
                    