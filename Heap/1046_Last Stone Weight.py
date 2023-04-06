class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for idx, s  in enumerate(stones):
            stones[idx] = s * -1
            
        heapq.heapify(stones)
        while(len(stones) > 1):
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            tmp = first - second
            if(tmp != 0):
                heapq.heappush(stones, tmp)
        stones.append(0)
        return abs(stones[0])