'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

 

示例 1：



输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def maxArea(self,height):#穷举组合超时
        a = None
        b = None
        _width = 0
        _height = 0
        area = 0
        data = [[] for i in range(len(height))]
        for x,y in enumerate(height):
            data[x].append(x)
            data[x].append(y)
        #data.sort(key=lambda x:x[1])#升序
        data.sort(key=lambda x:x[1],reverse=True)#降序
        #print(data)
        for i,j in enumerate(data):
            if j[0] < _width and abs(j[0] - len(height) + 1) < _width and j[1] < _height:#当前数据点到左右的宽度以及高度都没有目前最优解大时，则进行跳过
                continue #跳过无用数据，优化时间
            for m,n in enumerate(data[i+1:]):
                square = abs(j[0]-n[0])*min(j[1],n[1])
                if square > area:
                    a = j
                    b = n
                    area = square
                    _width = abs(j[0]-n[0])
                    _height = min(j[1],n[1])
        print(a,b,area)
        return area
    
    def maxArea2(self,height):#双指针
        left = 0
        right = len(height) - 1
        area = 0
        pos1 = None
        pos2 = None
        while left < right:
            square = (right - left) * min(height[left],height[right])
            if square > area:#更新面积值
                area = square
                pos1 = (left,height[left])
                pos2 = (right,height[right])
            if height[left] > height[right]:#总是移动较小的指针
                right -= 1
            else:
                left += 1
        print(pos1,pos2,area)
        return area

s = Solution()
s.maxArea2([9,41,12,13,5,14,40])