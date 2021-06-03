'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def threeSumClosest(self, nums, target):#超出时间限制
        if not nums or len(nums) < 3:
            return
        MAX_INT = 2**31-1
        dis = MAX_INT #误差值
        result_list = None
        result = None
        nums.sort()#默认升序
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if abs(nums[i]+nums[j]+nums[k] - target) < dis:
                        dis = abs(nums[i]+nums[j]+nums[k] - target)
                        result_list = [nums[i],nums[j],nums[k]]
                        result = nums[i]+nums[j]+nums[k]
        print(result_list,result)
        return result
    def threeSumClosest2(self, nums, target):#双指针
        if not nums or len(nums) < 3:
            return
        MAX_INT = 2**31-1
        dis = MAX_INT #误差值
        result_list = None
        result = None
        nums.sort()#默认升序
        for i in range(len(nums)):
            L = i+1
            R = len(nums) - 1
            while(L < R):
                sum = nums[i]+nums[L]+nums[R]
                if sum == target:
                    print(nums[i],nums[L],nums[R])
                    return target
                else:
                    if abs(sum-target) < dis:
                        dis = abs(sum-target)
                        result_list = [nums[i],nums[L],nums[R]]
                        result = sum
                    if sum > target:
                        R -= 1
                    else:#sum < target:
                        L += 1
                
            
        print(result_list,result)
        return result
s = Solution()
s.threeSumClosest2([-1,2,1,-4],1)


