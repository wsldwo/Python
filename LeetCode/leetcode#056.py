class Solution:
    '''
    执行结果：通过
    执行用时：64 ms, 在所有 Python3 提交中击败了12.80%的用户
    内存消耗：15.7 MB, 在所有 Python3 提交中击败了17.36%的用户
    第二次终于通过了！！！
    '''
    def merge(self, intervals):
        res = [] # 结果集
        def merge_intervals(iv1,iv2):
            if iv1[1] < iv2[0] or iv2[1] < iv1[0]:#无交集
                return None
            if iv1[1] >= iv2[0] and iv1[1] <iv2[1] and iv2[0] > iv1[0]: return [iv1[0],iv2[1]]#交叉
            if iv2[1] >= iv1[0] and iv2[1] <iv1[1] and iv1[0] > iv2[0]: return [iv2[0],iv1[1]]#交叉
            if iv1[1] == iv2[1]:#右端点相等
                if iv1[0] < iv2[0]:
                    return [iv1[0],iv1[1]]
                else:
                    return [iv2[0],iv2[1]]
            if iv1[0] == iv2[0]:#左端点相等
                if iv1[1] > iv2[1]:
                    return [iv1[0],iv1[1]]
                else:
                    return [iv2[0],iv2[1]]
            if iv1[0] >= iv2[0] and iv1[1] <= iv2[1]: return [iv2[0],iv2[1]]#包含
            if iv2[0] >= iv1[0] and iv2[1] <= iv1[1]: return [iv1[0],iv1[1]]#包含
            return None
        def do_merge(ivs,res):
            left_intervals = []
            civ = ivs[0]
            for i in range(1,len(ivs)):
                r = merge_intervals(civ,ivs[i])
                if r != None:
                    civ = r
                else:
                    left_intervals.append(ivs[i])
            #civ已无法与其它列表合并
            #print(f'civ: {civ}')
            res.append(civ)
            #print(f'res: {res}')
            #print(f'left_intervals: {left_intervals}')
            return left_intervals
        
        lein = do_merge(intervals,res)
        first_time = True
        while True:
            res_len1 = len(res)
            if first_time:
                first_time = False
            else:
                lein = res.copy()
                res.clear()
            #print(f'res_len1: {res_len1}')
            #print(f'lein: {lein}')
            while len(lein) >= 1:
                lein = do_merge(lein,res)
            
            res_len2 = len(res)
            #print(f'res_len2: {res_len2}')

            if res_len2 == res_len1:
                break
        print(f'res: {res}')
        return res

s = Solution()
s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]])

