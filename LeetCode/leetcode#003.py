class Solution:
    def lengthOfLongestSubstring(self,s):
        #dict1 = {}
        maxstr = ''
        maxlen = 0
        for i in range(len(s)):
            set1 = set()
            str1 = ''
            for y in s[i:]:
                if y not in set1:
                    set1.add(y)
                    str1+=y
                else:
                    break
            if len(str1)>maxlen:
                maxstr = str1
                maxlen = len(str1)
        '''
            dict1[str1] = len(str1)
        maxstr = ''
        maxlen = 0
        for k,v in dict1.items():
            if v > maxlen:
                maxstr = k
                maxlen = v
        '''
        print(maxstr,maxlen)
        return maxlen
    def lengthOfLongestSubstring2(self,s):
        '''
        双指针滑窗
        定义两个指针，一个左指针，一个右指针，从长串开头，先移动右指针，获取一个字符，
        如果“窗口”（即两指针间）里没有重复的字符，继续向右移右指针；
        直到遇上“窗口”中已包含的字符，右指针等待；
        开始移动左指针，每移动一次，看看现“窗口”中是否还包含右指针所指的字符；
        直到“窗口”中没有右指针所指字符，就停止移动左指针，接着继续移动右指针。
        重复以上步骤，直到有一个指针（一般是右指针）移动到长串边界，结束。
        在这个过程中随时记录“窗口”最大时的情况，即是我们的答案。
        '''
        i = 0#左指针
        j = 0#右指针
        maxstr = ''
        maxlen = 0
        while(j<len(s)):#防止越界
            while(j<len(s) and s[j] not in s[i:j]):
                #print('j:',j)
                j += 1#右指针移动
            if len(s[i:j]) > maxlen:
                maxstr = s[i:j]
                maxlen = len(s[i:j])
                #print(maxstr,maxlen)
            i += 1#左指针移动
        print('maxstr:',maxstr,'maxlen:',maxlen)
        return maxlen



s = Solution()
s.lengthOfLongestSubstring2('pwwkewawjdoawdiadjjdjdiwo')
#print('k' in 'kkk'[0:0],'k' in 'kkk'[1:1],) #False False
