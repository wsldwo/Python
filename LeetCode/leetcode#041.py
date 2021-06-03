class Solution:
    #找出其中没有出现的最小的正整数
    def firstMissingPositive(self, nums):

        def merge_sort(nums,nums_copy,start,end):
            if start >= end:
                return
            
            start1 = start
            end1 = (start + end) // 2
            start2 = end1 + 1
            end2 = end

            merge_sort(nums,nums_copy,start1,end1)
            merge_sort(nums,nums_copy,start2,end2)

            k = start

            while(start1 <= end1 and start2 <= end2):
                if nums[start1] < nums[start2]:
                    nums_copy[k] = nums[start1]
                    k += 1
                    start1 += 1
                else:
                    nums_copy[k] = nums[start2]
                    k += 1
                    start2 += 1
            
            while(start1 <= end1):
                nums_copy[k] = nums[start1]
                k += 1
                start1 += 1
            while(start2 <= end2):
                nums_copy[k] = nums[start2]
                k += 1
                start2 += 1
            
            for i in range(start,end + 1):
                nums[i] = nums_copy[i]

        print(f'before sort:{nums}')

        nums_copy = nums.copy()

        merge_sort(nums,nums_copy,0,len(nums) - 1)

        print(f'after sort:{nums}')

        length = len(nums)

        if length == 0:
            return 1

        if length == 1:
            if nums[0] < 1:
                return 1
            if nums[0] > 1:
                return 1
            if nums[0] == 1:
                return 2
        
        if 1 not in nums:
            return 1

        last_negative = None
        first_positive = None
        ans = -9999

        if nums[0] > 1:
            return 1
        if nums[-1] < 0:
            return 1
        

        for i in range(length - 1):
            if nums[i] < 0:
                last_negative = nums[i]
            if nums[i] > 0 and first_positive == None:
                first_positive = nums[i]
            
            if last_negative != None and first_positive != None:
                if first_positive > 1:
                    ans = 1
                    break


            if nums[i] >= 0 and nums[i + 1] - nums[i] > 1:
                ans = nums[i] + 1
                break
            if i == length - 2:
                ans = nums[i + 1] + 1
                break
        print(f'last_negative: {last_negative}  first_positive: {first_positive}')
        return ans


        


    



s = Solution()
print(s.firstMissingPositive([-1,-2,-60,40,43]))
                





