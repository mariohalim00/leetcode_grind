class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret_val = []
        for idx, num in enumerate(nums):
            if(idx > 0 and nums[idx] == nums[idx - 1]):
                continue
            l = idx + 1
            r = len(nums) - 1
            while(r > l):
                threeSum = nums[l] + nums[r] + num
                # print("curr. ", num, threeSum)
                if(threeSum < 0): l += 1
                elif(threeSum > 0): r -= 1
                else:
                    ret_val.append([num, nums[l], nums[r]])
                    l+=1
                    # print(l)
                    while (l < r and nums[l] == nums[l - 1]):
                        l+=1

        return ret_val


# SOLUTION 2 (PRONE TO EXCEEDING TIME LIMIT AND OR MEMORY)
# class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     ret_val = []
    #     for idx, num in enumerate(nums):
    #         l = idx + 1
    #         r = len(nums) - 1
    #         while(r > l):
    #             threeSum = nums[l] + nums[r] + num
    #             if(threeSum > 0): l += 1

    #     return ret_val


# MY ORIGINAL WORKING SOLUTION
# # NOT THE FASTEST
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         a = 0
#         b = a + 1
#         c = len(nums) - 1
#         res = []
#         # print(nums)
#         while(b < c):
#             remainder = 0 - nums[a]
#             while(b < c):
#                 tmp = nums[b] + nums[c]
#                 # print(tmp, remainder, b , c)
#                 if(tmp < remainder):
#                     b += 1
#                 elif(tmp > remainder):
#                     c -= 1
#                 else:
#                     # print(tmp, remainder)
#                     item = [nums[a], nums[b], nums[c]]
#                     if(item not in res):
#                         res.append(item)
#                         b += 1
#                     else:
#                         b += 1
#                     continue
#             # print("nenen-", a)
#             a += 1
#             b = a + 1
#             c = len(nums) - 1
#         return res