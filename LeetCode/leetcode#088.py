class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #解法1 插入排序
        '''
        执行结果：通过
        执行用时：48 ms, 在所有 Python3 提交中击败了15.49%的用户
        内存消耗：14.6 MB, 在所有 Python3 提交中击败了96.26%的用户
        '''
        def insert_sort(nums1,m,nums2,n):
            for i in range(m,m + n):# 外层是插入位置
                temp = nums2[i - m]
                j = i - 1 # 向前方插入
                while j >= 0 and nums1[j] > temp:
                    nums1[j + 1] = nums1[j] #数据后移
                    j -= 1
                if j >= 0: 
                    nums1[j + 1] = temp #进行插入
                else:
                    nums1[0] = temp #在第一个位置插入
        #insert_sort(nums1,m,nums2,n)
        #解法2 归并排序 空间换时间
        '''
        执行结果：通过
        执行用时：44 ms, 在所有 Python3 提交中击败了36.52%的用户
        内存消耗：14.9 MB, 在所有 Python3 提交中击败了42.07%的用户
        '''
        def merge_sort(nums1,m,nums2,n):
            res = [0] * (m + n)
            i = 0
            start1,start2 = 0,0
            while start1 < m and start2 < n:
                if nums1[start1] < nums2[start2]:
                    res[i] = nums1[start1]
                    start1 += 1
                else:
                    res[i] = nums2[start2]
                    start2 += 1
                i += 1
            while start1 < m:
                res[i] = nums1[start1]
                i += 1
                start1 += 1
            while start2 < n:
                res[i] = nums2[start2]
                i += 1
                start2 += 1
            for j in range(m + n):
                nums1[j] = res[j]
        merge_sort(nums1,m,nums2,n)


