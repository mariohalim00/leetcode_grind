class Solution:
    def distanceFromOrigin(self, point: List[int]):
        x = point[0]
        y = point [1]
        
        tmp_x = (x - 0 ) ** 2
        tmp_y = (y - 0) ** 2
        temp = tmp_x + tmp_y
        
        return math.sqrt(temp)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if(k == len(points)):
            return points
        minHeap = []
        ret = []
        heapq.heapify(minHeap)
        for p in points:
            temp = self.distanceFromOrigin(p)
            heapq.heappush(minHeap, [temp, p[0], p[1]])
            # this is n log n, can do better by appending first and then heapify later
            
        for i in range(k):
            dist, x, y =  heapq.heappop(minHeap)
            ret.append([x, y])
            
        return ret
            