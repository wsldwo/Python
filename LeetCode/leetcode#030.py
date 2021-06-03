'''
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    '''
    执行用时：9932 ms, 在所有 Python3 提交中击败了5.06%的用户
    内存消耗：15.2 MB, 在所有 Python3 提交中击败了54.89%的用户
    '''
    def findSubstring(self, s: str, words: [str]) -> [int]:
        result = []
        s_len = len(s)
        words_len = len(words)
        if s_len == 0 or words_len == 0:
            return result
        single_word_len = len(words[0])
        total_words_len = words_len * single_word_len

        def check(ss):
            words_copy = words.copy()
            for i in range(0,total_words_len,single_word_len):
                sss = ss[i:i+single_word_len]
                if sss in words_copy:
                    words_copy.remove(sss)
                else:
                    return False
            if len(words_copy) == 0:
                return True
            else:
                return False

        for i in range(s_len):
            if check(s[i:i+total_words_len]):
                result.append(i)
        
        return result