from random import random,randint
def swap(nums,i,j):
    if i == j:
        return
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
def quick_sort(nums,start,end):#单路快排
    if start < end:
        pivot = nums[start] #默认取第一个数为pivot
        i,j = start,end #左右指针
        #挖坑填数
        while i < j:
            #首先从右向左扫描比pivot小的数字放到前边
            while i < j and pivot <= nums[j]:
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1
            #然后从左向右扫描比pivot大的数字放到后边
            while i < j and pivot >= nums[i]:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1
        #循环跳出时，i == j
        nums[i] = pivot #补上pivot
        quick_sort(nums,start,i - 1)
        quick_sort(nums,i + 1,end)
def quick_sort2(nums,start,end):#双路快排
    if start < end:
        pivot = nums[start]
        i,j = start + 1,end
        while True:
            while i <= end and nums[i] < pivot:
                i += 1
            while j >= start + 1 and nums[j] > pivot:
                j -= 1
            if i < j:
                swap(nums,i,j)
                i += 1
                j -= 1
            else:
                break   
        #循环跳出时,j指向最后一个小于pivot的数字，i指向第一个大于pivot的数字
        swap(nums,start,j)
        quick_sort2(nums,start,j - 1)
        quick_sort2(nums,j + 1,end)

def quick_sort3(nums,start,end):#三路快排
    if start < end:
        if end - start + 1 < 15:#快排优化2：元素数量低于15个时，采取插入排序会更好
            print('快排优化2:元素数量低于15个时，采取插入排序')
            #插入排序
            for j in range(start + 1,end + 1):# 从第二个元素开始插入，切记 range函数 “前闭后开”
                temp = nums[j]
                for k in range(j - 1,start - 1, -1):
                    if nums[k] > temp:
                        nums[k + 1] = nums[k] #后移
                        if k == start: #边界情况
                            nums[k] = temp
                    else:
                        nums[k + 1] = temp #插入数据，跳出后，进行下一次插入
                        break

            return
        rndpos = int(random() * (end - start + 1) + start)
        print('快排优化1：rndpos: ',rndpos, ' start: ',start,' end: ',end,' pivot:',nums[rndpos])
        swap(nums,start,rndpos) #快排优化1：取随机位置作为pivot，把它和第一个元素交换一下
        pivot = nums[start]
        i = start + 1 #从第二个元素开始
        lt,gt = start,end + 1 #lt指向最后一个小于pivot的数，gt指向第一个大于pivot的数，lt和gt中间时等于pivot
        while True:
            if nums[i] == pivot:
                i += 1
            elif nums[i] < pivot:
                swap(nums,i,lt + 1)
                lt += 1
                i += 1
            else: #nums[i] > pivot:
                swap(nums,i,gt - 1)
                gt -= 1
                #注意此处无需 i += 1，因为上边是把未知元素交换到前边来了
            if i == gt:
                break
        swap(nums,start,lt)
        quick_sort3(nums,start,lt - 1)#由于上边的交换，lt此时指向等于pivot的第一个元素
        quick_sort3(nums,gt,end)
    

nums = [-9,10,-44,7,25,8,-1000,1500,99,100,10,6,8,25,1,-3,97,584,0,-1,189,600,660,-20,8848,100,8]
quick_sort3(nums,0,len(nums) - 1)
print(nums)