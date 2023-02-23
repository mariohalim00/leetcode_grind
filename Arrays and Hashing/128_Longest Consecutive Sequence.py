class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_length = 0

        for num in nums:
            left_consecutive_element = num - 1
            length = 0
            # check if the left_consecutive element exist in the 
            # if it does not exist it means it is the start of the sequence
            if (left_consecutive_element not in nums_set):
                # keep increasing the length while the current number + length exists in the set
                # if it no longer exist, it means we have reached the end of the sequence
                consecutive_element = num + length
                while(consecutive_element in nums_set):
                    length += 1
                    consecutive_element = num + length
            # get the max value of the current length and the current longest
            longest_length = max(longest_length, length)
        return longest_length

