class Solution:
    '''
    执行结果：通过
    执行用时：44 ms, 在所有 Python3 提交中击败了73.47%的用户
    内存消耗：16.4 MB, 在所有 Python3 提交中击败了20.36%的用户
    '''
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        print(f'intervals old: {intervals}')
        #start = -1 #记录开始索引
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                intervals.insert(i,newInterval)
                #start = i
                break
        if newInterval not in intervals:#防止未插入
            intervals.append(newInterval)
        print(f'intervals new: {intervals}')
        '''
        iv = intervals[start]
        end = -1 #记录结束索引
        for i in range(start,len(intervals)):
            if iv[1] < intervals[i][0]:
                #无交集
                end = i - 1
                break
            iv[1] = max(iv[1],intervals[i][1])

        res = intervals[:start]
        res.append(iv)
        res += intervals[end + 1:]
        '''
        res = []
        for i in range(len(intervals)):
            if not res or res[-1][1] < intervals[i][0]: #没有交集，直接添加，可合并区间一定连续
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1],intervals[i][1]) #合并区间，取较大的右端点
        print(res)
        return res


s = Solution()
s.insert([[1,5]],[2,7])