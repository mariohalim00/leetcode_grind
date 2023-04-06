class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        m = (l + r) // 2
        k = None
        while (l <= r):
            m = (l + r) // 2
            tmp = m
            count = 0
            for i in piles:
                count += math.ceil(i / tmp)

            if(count > h):        
                l = m + 1
            elif(count < h):
                r = m - 1
            else:
                if(not k):
                    k = tmp
                else:
                    k = min(k, tmp)
                r = m - 1
        if(k == None):
            return( math.ceil( ( l + r ) / 2 ) )
        return k