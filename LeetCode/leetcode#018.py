'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：答案中不可以包含重复的四元组。

 

示例 1：

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：

输入：nums = [], target = 0
输出：[]
 

提示：

0 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def fourSum(self, nums, target):#双指针
        if not nums or len(nums) < 4:
            return []
        result = []
        nums_len = len(nums)
        nums.sort()#默认升序
        for i in range(nums_len-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[nums_len-3] + nums[nums_len-2] + nums[nums_len-1] < target:
                continue
            for j in range(i+1,nums_len-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[nums_len-2] + nums[nums_len-1] < target:
                    continue
                L,R = j+1,nums_len-1
                while(L<R):
                    total = nums[i]+nums[j]+nums[L]+nums[R]
                    if total == target:
                        result.append([nums[i],nums[j],nums[L],nums[R]])
                        while L<R and nums[L] == nums[L+1]:
                            L+=1
                        while L<R and nums[R] == nums[R-1]:
                            R-=1
                        L+=1
                        R-=1
                    elif total<target:
                        L+=1
                    else:
                        R-=1
        return result

s = Solution()
print(s.fourSum([1,0,-1,0,-2,2],0))