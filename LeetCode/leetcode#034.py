class Solution:
    def searchRange(self, nums, target):
        start_pos = -1
        end_pos = -1

        if len(nums) == 0:
            return [-1,-1]
        
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]

        def divide_search(nums,target,start,end):
            print(f'start: {start}  end: {end}')

            if start > end or target > nums[end] or target < nums[start] : #start > end 要放到前面
                return -1
            middle = (start + end) // 2
            print('middle: %d' % middle)
            if nums[middle] > target:
                return divide_search(nums,target,start,middle - 1)
            elif nums[middle] < target:
                return divide_search(nums,target,middle + 1,end)
            else:
                #不能直接返回Middle
                #细节，有可能前面或者后面的也等于target
                if start_pos == -1:#如果前面还没找到
                    while middle >= 0 and nums[middle] == target:
                        middle -= 1
                    return middle + 1
                else:#如果前面已经找到
                    while middle >= 0 and middle < len(nums) and nums[middle] == target:
                        middle += 1
                    return middle - 1

        start_pos = divide_search(nums,target,0,len(nums) - 1)

        if start_pos == -1:
            return [-1,-1]
        else:
            print(f'start_pos: {start_pos}')
            end_pos = divide_search(nums,target,start_pos + 1,len(nums) - 1)
            print(f'end_pos: {end_pos}')
            if end_pos == -1:
                return [start_pos,start_pos]
            else:
                return [start_pos,end_pos]


s = Solution()
print(s.searchRange([1,4],4))