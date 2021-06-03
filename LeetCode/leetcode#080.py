class Solution:
    '''
    执行结果：通过
    执行用时：40 ms, 在所有 Python3 提交中击败了79.65%的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了72.75%的用户
    仅使用O(1)空间，因为只是用了len_nums变量记录列表长度
    '''
    def removeDuplicates(self, nums) -> int:
        len_nums = len(nums)
        if len_nums < 3:
            return len_nums
        i = 2
        while i < len_nums:
            if nums[i] == nums[i - 1] == nums[i - 2]:
                del nums[i] #删除索引为i这项后，i是不能变的，因为此时nums[i]是一个新的数，可以理解成后面的数往前挪了一位
                len_nums -= 1
            else:
                i += 1
        print('length: ',len_nums,' nums:',nums)
        return len_nums
    
    '''
    看了下评论区，居然有通过赋值来代替删除的思路，简直是妙啊！
    执行结果：通过
    执行用时：36 ms, 在所有 Python3 提交中击败了93.07%的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了13.00%的用户
    '''
    def removeDuplicates2(self, nums) -> int:
        i = 0 # i指向即将被赋值的位置
        for num in nums:
            if i < 2 or num > nums[i - 2]:
                nums[i] = num
                i += 1
        return i - 1
s = Solution()
s.removeDuplicates2([1,1,1,2,2,3])

