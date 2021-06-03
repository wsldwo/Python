class Solution:
    '''
    执行结果：通过
    执行用时：40 ms, 在所有 Python3 提交中击败了72.19%的用户
    内存消耗：15.2 MB, 在所有 Python3 提交中击败了71.72%的用户
    二分法变式，由于不知道分界点在哪边，所以需要进行判断，看起来比较臃肿
    没考虑到，左、中、右取值相等的特殊情况，第一次提交失败了
    '''
    def search(self, nums, target) -> bool:
        def binary_serach(nums,start,end,target,clear):
            print(nums[start:end + 1])
            if start > end:
                return
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            if clear:#当前区间已不包含分界点，即是一个升序区间
                if nums[middle] > target:
                    return binary_serach(nums,start + 1,middle - 1,target,True)
                elif nums[middle] < target:
                    return binary_serach(nums,middle + 1,end - 1,target,True)
            else:
                '''
                Bug 修正：左、中、右取值相等时，需要进一步讨论，分界点在哪边
                '''
                if nums[start] == nums[middle] == nums[end]:#特殊情况无法判断分界点在哪个区间
                    for i in range(start + 1,middle):
                        #分界点在左边
                        if nums[i] != nums[middle]:
                            if nums[i] == target:
                                return i
                            elif nums[i] > target:
                                return
                            else:
                                return binary_serach(nums,i + 1,middle - 1,target,True)
                    #分界点在右边
                    return binary_serach(nums,middle + 1,end - 1,target,False)

                #当前区间包含分界点，即由两段升序区间构成
                #分界点在左区间
                if nums[start] >= nums[middle] and nums[middle] <= nums[end]:
                    if nums[middle] > target:
                        return binary_serach(nums,start + 1,middle - 1,target,False)
                    elif nums[middle] < target:
                        if nums[end] < target:
                            return binary_serach(nums,start + 1,middle - 1,target,False)
                        elif nums[end] > target:
                            return binary_serach(nums,middle + 1,end - 1,target,True)
                #分界点在右区间
                elif nums[start] <= nums[middle] and nums[middle] >= nums[end]:
                    if nums[middle] < target:
                        return binary_serach(nums,middle + 1,end - 1,target,False)
                    elif nums[middle] > target:
                        if nums[start] < target:
                            return binary_serach(nums,start + 1,middle - 1,target,True)
                        elif nums[start] > target:
                            return binary_serach(nums,middle + 1,end - 1,target,False)
        res = binary_serach(nums,0,len(nums) - 1,target,False)
        if res != None:
            print('res: ',res,' True')
            return True
        else:
            print('res: ',res,' False')
            return False
    '''
    执行结果：通过
    执行用时：52 ms, 在所有 Python3 提交中击败了9.78%的用户
    内存消耗：15.5 MB, 在所有 Python3 提交中击败了5.00%的用户
    把代码简化了，速度却下降了。。。。
    '''
    def search2(self, nums, target) -> bool:
        def binary_serach(nums,start,end,target):
            if start > end:
                return
            middle = (start + end) // 2
            if nums[start] == target:
                return start
            if nums[middle] == target:
                return middle
            if nums[end] == target:
                return end
            if nums[start] < nums[middle] and nums[middle] < nums[end]:
                #区间有序，无分界点
                if nums[middle] > target:
                    return binary_serach(nums,start + 1,middle - 1,target)
                else:
                    return binary_serach(nums,middle + 1,end - 1,target)
            elif nums[start] > nums[middle] and nums[middle] < nums[end]:
                #左区间无序，右区间有序
                if nums[middle] < target and target < nums[end]:
                    return binary_serach(nums,middle + 1,end - 1,target)
                else:
                    return binary_serach(nums,start + 1,middle - 1,target)
            elif nums[start] < nums[middle] and nums[middle] > nums[end]:
                #右区间无序，左区间有序
                if nums[start] < target and target < nums[middle]:
                    return binary_serach(nums,start + 1,middle - 1,target)
                else:
                    return binary_serach(nums,middle + 1,end - 1,target)
            else:#无法判断区间是否有序，左右各减1
                return binary_serach(nums,start + 1,end - 1,target)
        res = binary_serach(nums,0,len(nums) - 1,target)
        if res != None:
            print('res: ',res,' True')
            return True
        else:
            print('res: ',res,' False')
            return False

s = Solution()
s.search2([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1],2)