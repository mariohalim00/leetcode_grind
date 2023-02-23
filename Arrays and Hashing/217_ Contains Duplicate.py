class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_checker = {}
        for item in nums:
            if item in duplicate_checker:
                return True
            else:
                duplicate_checker[item] = 1