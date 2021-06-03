'''
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

示例 1：

输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
示例 2：

输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    '''
    执行用时：3828 ms, 在所有 Python3 提交中击败了5.01%的用户
    内存消耗：15.8 MB, 在所有 Python3 提交中击败了40.35%的用户
    '''
    def removeDuplicates(self, nums):
        if not nums or len(nums) == 0:
            return 0
        print(nums)
        for x in nums:
            while nums.count(x) > 1:
                nums.remove(x)
        print(nums)
        return len(nums)
    '''
    执行用时：52 ms, 在所有 Python3 提交中击败了44.40%的用户
    内存消耗：15.8 MB, 在所有 Python3 提交中击败了29.46%的用户
    '''
    def removeDuplicates2(self, nums):
        if not nums or len(nums) == 0:
            return 0
        print(nums)
        nums2 = []
        nums2.append(nums[0])
        for i in range(1,len(nums),1):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums2.append(nums[i])
        nums.clear()
        nums += nums2
        print(nums)
        return len(nums)
    '''
    官方解法：快慢指针法
    '''
    def removeDuplicates3(self, nums):
        if not nums:
            return 0
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return 1
        slow = 0
        quick = 1
        while quick < length:
            if nums[slow] != nums[quick]:
                slow += 1
                nums[slow] = nums[quick]
            quick += 1
        return slow + 1



s = Solution()
s.removeDuplicates2([1,1,2,4,4,4,7,11,14,14])
