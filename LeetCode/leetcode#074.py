class Solution:
    '''
    执行结果：通过
    执行用时：48 ms, 在所有 Python3 提交中击败了16.48%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了69.19%的用户
    两次二分法
    '''
    def searchMatrix(self, matrix, target):
        if matrix[0][0] > target:
            return False
        if matrix[-1][-1] < target:
            return False
        def binarySearch_matrix(matrix,start,end,target):
            if start >= end:
                return start
            middle = (start + end) // 2
            if matrix[middle][0] > target:
                return binarySearch_matrix(matrix,start,middle - 1,target)
            elif matrix[middle][-1] < target:
                return binarySearch_matrix(matrix,middle + 1,end,target)
            else:
                return middle
        key = binarySearch_matrix(matrix,0,len(matrix) - 1,target)
        def binarySearch_target(interval,start,end,target):
            if start >= end:
                return start
            middle = (start + end) // 2
            if interval[middle] > target:
                return binarySearch_target(interval,start,middle - 1,target)
            elif interval[middle] < target:
                return binarySearch_target(interval,middle + 1,end,target)
            else:
                return middle
        ans = binarySearch_target(matrix[key],0,len(matrix[0]) - 1,target)
        if matrix[key][ans] == target:
            return True
        return False

