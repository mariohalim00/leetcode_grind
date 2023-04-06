class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for n in nums:
            minHeap.append(-n)
        
        heapq.heapify(minHeap)
        tmp = None
        for i in range(k):
            tmp = heapq.heappop(minHeap)
        
        return tmp * -1