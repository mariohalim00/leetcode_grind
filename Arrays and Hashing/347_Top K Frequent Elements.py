class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if(len(nums) == 0): return []
        
        freq_hash = {}
        for i in nums:
            if i not in freq_hash:
                freq_hash[i] = 1
            else:
                freq_hash[i] += 1

        sorted_freq_hash = {key: val for key, val in sorted(freq_hash.items(), key = lambda ele: ele[1], reverse = True)}
        
        ret_val = []
        for i in sorted_freq_hash.keys():
            if k == 0: break
            ret_val.append(i)
            k -= 1
        return ret_val
