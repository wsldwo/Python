class Solution:
    def search(self, nums, target) -> int:
        if (len(nums) == 1):
            if nums[0] == target:
                return 0
            else:
                return -1
        #先找到分界点
        boundary = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                boundary = i
                break
        print(f'boundary: {boundary}')
        left_area = nums[:boundary + 1]
        right_area = nums[boundary + 1:]
        #二分法
        def divide_search(nums,target,start,end):
            if target > nums[end] or target < nums[start] or start > end:
                return -1
            
            middle = (start + end) // 2
            if nums[middle] > target:
                return divide_search(nums,target,start,middle - 1)
            elif nums[middle] < target:
                return divide_search(nums,target,middle + 1,end)
            else:
                return middle

        left_pos = divide_search(left_area,target,0,len(left_area) - 1)
        right_pos = divide_search(right_area,target,0,len(right_area) - 1) 

        if right_pos != -1:
            right_pos +=  boundary + 1

        if left_pos >= 0:
            return left_pos
        else:
            return right_pos

s = Solution()
print(s.search([1],3))
            

        


