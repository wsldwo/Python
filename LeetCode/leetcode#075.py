class Solution:
    '''
    执行结果：通过
    执行用时：48 ms, 在所有 Python3 提交中击败了15.36%的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了8.49%的用户
    自己写的归并排序，有点慢！！！
    归并排序的缺点，需要使用O(N)的额外数组空间
    '''
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        def merge_sort(nums,nums_copy,start,end):
            if start >= end:
                return
            start1 = start
            end1 = (start + end) // 2
            start2 = end1 + 1
            end2 = end
            merge_sort(nums,nums_copy,start1,end1)
            merge_sort(nums,nums_copy,start2,end2)
            k = start
            while start1 <= end1 and start2 <= end2:
                if nums[start1] < nums[start2]:
                    nums_copy[k] = nums[start1]
                    start1 += 1
                else:
                    nums_copy[k] = nums[start2]
                    start2 += 1
                k += 1
            while start1 <= end1:
                nums_copy[k] = nums[start1]
                start1 += 1
                k += 1
            while start2 <= end2:
                nums_copy[k] = nums[start2]
                start2 += 1
                k += 1
            for i in range(start,end + 1):
                nums[i] = nums_copy[i]
        nums_copy = nums.copy()
        merge_sort(nums,nums_copy,0,len(nums) - 1)
    '''
    执行结果：通过
    执行用时：28 ms, 在所有 Python3 提交中击败了99.00%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了11.91%的用户
    很久没写快速排序了，大概流程还是记得
    归并和快排在循环条件上的区别是：归并 start <= end (要带等号，因为要完整地归并数字)  快排 i < j (不带等号，循环跳出时i == j，此时插入pivot)
    '''
    def sortColors2(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        def quick_sort(nums,start,end):#单路快排
            if start < end:
                pivot = nums[start] #默认取第一个数为pivot
                i,j = start,end #左右指针
                #挖坑填数
                while i < j:
                    #首先从右向左扫描比pivot小的数字放到前边
                    while i < j and pivot <= nums[j]:
                        j -= 1
                    if i < j:
                        nums[i] = nums[j]
                        i += 1
                    #然后从左向右扫描比pivot大的数字放到后边
                    while i < j and pivot >= nums[i]:
                        i += 1
                    if i < j:
                        nums[j] = nums[i]
                        j -= 1
                #循环跳出时，i == j
                nums[i] = pivot #补上pivot
                quick_sort(nums,start,i - 1)
                quick_sort(nums,i + 1,end)
        def quick_sort2(nums,start,end):#双路快排
            pass
        def quick_sort3(nums,start,end):#三路快排
            pass
        quick_sort(nums,0,len(nums) - 1)

    
                
