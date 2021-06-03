'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def threeSum(self, nums):#超出时间限制
        first_r = self.C(nums,len(nums),3)
        second_r = []
        result = []
        print(first_r)
        for x in first_r:
            if set(x) not in second_r:
                result.append(x)
                second_r.append(set(x))
        print(result)
        return result

        #要如何对列表去重呢？
    def C(self,sequence,n,m,result=[]):
        if type(sequence) != type([]): # 类型检查
            return []
        if n < m: # 参数合法性检查
            return []
        if m == 0:
            #print(result)
            return [result]
        if len(result) == 2:
            if -result[0]-result[1] not in sequence:
                return []
            else:
                return[[result[0],result[1],-result[0]-result[1]]]
        all_results = []
        for index,value in enumerate(sequence):
            r = self.C(sequence[index+1:],n,m-1,result+[value])
            all_results.extend(r)
        return all_results

    def threeSum2(self, nums):#双指针
        if not nums or len(nums) < 3:
            return []
        if nums.count(0) == len(nums):
            print([0,0,0])
            return [0,0,0]
        result = []
        nums.sort()#默认升序
        for k,v in enumerate(nums):
            if v > 0:
                return result
            if k > 0 and v == nums[k-1]:#跳过重复元素
                continue
            L = k + 1
            R = len(nums) - 1
            while(L < R):
                if v + nums[L] + nums[R] == 0:
                    result.append([v,nums[L],nums[R]])
                    print(result)
                    while(L < R and nums[L] == nums[L + 1]):#跳过重复元素
                        L += 1
                    while(L < R and nums[R] == nums[R - 1]):#跳过重复元素
                        R -= 1
                    L += 1
                    R -= 1
                elif v + nums[L] + nums[R] > 0:
                    R -= 1
                else:
                    L += 1
        return result

s = Solution()
s.threeSum2([-1,0,1,2,-1,-4])

print([-1,0,1]==[0,1,-1])
print(set([-1,0,1])==set([0,1,-1]))
print(set([0,1,-1]) in [set([-1,0,1]),set([-1,2,-1]),set([0,1,-1])])