class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # isolate row (log O(n))
        l, r = 0, len(matrix) - 1
        mid, row = 0, 0
        while(l < r):
            mid =  (l + r + 1) // 2
            print(l, r, mid)
            if(mid == l == r): break
            if(target < matrix[mid][0]):
                r = mid - 1
                l = l
            elif(target == matrix[mid][0]):
                return True
            else:
                if(target == matrix[mid][-1]):
                    return True
                elif(target > matrix[mid][-1]):
                    l = mid + 1
                    r = r
                else:
                    r = l = mid

        row = l
        
        if(row >= len(matrix)): return False
        # search
        l, r, mid = 0, len(matrix[row]) - 1, 0
        while(l <= r):
            mid =  (l + r + 1) // 2
            if(target == matrix[row][l]): return True
            elif(target == matrix[row][r]): return True
            elif(target == matrix[row][mid]): return True
            elif(l == r): break
            elif(target > matrix[row][mid]):
                l = mid + 1
                r = r
            elif(target < matrix[row][mid]):
                r = mid - 1
                l = l
        
        return False

