class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while(l <= r):
            mid = ( l + r + 1) // 2
            if(target == nums[mid]):
                return mid
            elif(target == nums[l]):
                return l
            elif(target == nums[r]):
                return r
            elif(l == r):
                break
            elif(target > nums[mid]):
                l = mid + 1
                r = r
            elif(target < nums[mid]):
                r = mid - 1
                l = l
            
        return -1