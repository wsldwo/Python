class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = nums1 + nums2
        print(nums3)
        nums3.sort()#默认升序
        print(nums3)
        #nums3.sort(reverse=True)#降序
        #print(nums3)
        len3 = len(nums3)
        result = None
        if len3 % 2 == 1:#奇数
            result = nums3[int((len3-1)/2)]
        else:#偶数
            result = (nums3[int(len3/2)] + nums3[int((len3/2)-1)])/2
        print(result)
        return result



s = Solution()
s.findMedianSortedArrays([2,4,6,8,10],[4,8,11,33])