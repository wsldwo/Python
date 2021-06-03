class Solution:
    def twoSum(self,nums,target):
        for i,x in enumerate(nums):
            for j,y in enumerate(nums):
                if i == j:
                    continue #同一元素只能用一次
                if x + y == target:
                    print(x,'+',y,'=',target)
                    return [i,j]
    def twoSum2(self,nums,target):
        dict = {}
        for i,x in enumerate(nums):
            d_num = target - x #差值
            if d_num in dict: #查找差值
                return [dict[d_num],i]
            else:
                dict[x] = i

s = Solution()
print(s.twoSum2([2,7,11,15],9))