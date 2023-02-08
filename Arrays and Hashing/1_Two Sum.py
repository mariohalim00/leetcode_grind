class Solution:
  #  Solution (8-Feb-2023) 
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     index_pair = []
    #     visited = {}
    #     for idx, value in enumerate(nums):
    #         remainder = target - value
    #         if remainder in visited:
    #             index_pair.append(idx)
    #             index_pair.append(visited[remainder])
    #             break
    #         else:
    #             visited[value] = idx
    #     print(index_pair)
    #     return index_pair 


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_output = {}
        for index, num in enumerate(nums):
            new_target = target - num
            if(new_target in dict_output.keys()):
                return [index, dict_output[new_target]]
            else:
                dict_output[num] = index
