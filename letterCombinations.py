"""
Question:
given an integer list containing digits from 0 to 9,
the task is to print all possible letter combinations that the numbers could represent.
A mapping of digit to letters is being followed.
note that 0 and 1 do not map to any letters.
the program need to support converting the digits from 0 to 99 into letters
"""


class LetterCombinations:
    def letterConbinations(self, digits):
        mapping = {0: [''],
                   1: [''],
                   2: ['a', 'b', 'c'],
                   3: ['d', 'e', 'f'],
                   4: ['g', 'h', 'i'],
                   5: ['j', 'k', 'l'],
                   6: ['m', 'n', 'o'],
                   7: ['p', 'q', 'r', 's'],
                   8: ['t', 'u', 'v'],
                   9: ['w', 'x', 'y', 'z']}

        # 如果是支持0-99的范围，先将两位数拆分称一位数，形成一个新的list
        newDigits = []
        for digit in digits:
            if 1-isinstance(digit, int) or digit < 0 or digit > 100:
                return "请输入0-99的范围内的整数："+repr(digit)
            elif 0 <= digit < 10:
                newDigits.append(digit)
            else:
                newDigits.append(int(digit / 10))
                newDigits.append(int(digit % 10))

        # res用于存放最终结果
        res = []
        # tmp用于存放单一组合好的元素
        tmp = ''
        # 先对特殊情况进行判断，防止程序异常停止
        if len(newDigits) == 0:
            return res

        # 递归
        def helper(tmp, digits):
            # 递归终止条件--列表digits遍历完成
            if len(digits) == 0:
                return res.append(tmp)
            # 单次递归--
            for letters in mapping[digits[0]]:
                helper(tmp + letters, digits[1:])

        # 调用递归
        helper(tmp, newDigits)
        return res


'''
通过用例
含有0、1不代表任何字母-->特殊测试：[0],[1],[0,1],[0,2,1]
正常测试：[2,3],[99,10]
输入非法数据：[9.1](小数）、[-2]（超出下界）、[100]（超出上界）
空列表
'''
if __name__ == '__main__':
    digits = []
    s = LetterCombinations()
    print(s.letterConbinations(digits))
