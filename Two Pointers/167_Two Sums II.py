class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while(j > i):
            curr_sum = numbers[i] + numbers[j]
            if(curr_sum < target): i+=1
            if(curr_sum > target): j-=1
            if(curr_sum == target): return [i + 1, j + 1]