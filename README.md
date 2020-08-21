# codingTest
**问题：**<br/>
&emsp;given an integer list containing digits from 0 to 9,
    the task is to print all possible letter combinations that the numbers could represent.
    A mapping of digit to letteers is being followed.
    note that 0 and 1 do not map to any letters.
    the program need to support converting the digits from 0 to 99 into letters.

    example:
        input:[2,3]-->output:['ad','ae','af','bd','be','bf','cd','ce','cf']


**问题理解：**<br/>
&emsp;input：输入一个有若干整数的**列表**<br/>
&emsp;output:输出列表中每个数字代表的字目的组合。<br/>
&emsp;附加条件：要满足0-99的输入<br/>

**解题思路：**<br/>
&emsp;观察example，如果list中有两个数字，那么可以用两个循环嵌套遍历数字对应字母的映射；如果有n个数字，则可以用n层循环嵌套，由此可以联想到用递归来实现。<br/>
&emsp;对于时间复杂度的话，主要在于递归中消耗的时间，在每一次递归中，需要循环3-4次，递归进行N次for循环，时间复杂度为O(4^N)<br/>
&emsp;对于程序要满足0-99的数字输入，非常简单的想法就是将数字依靠位数分割（求余和取模），由于规定了最大只有两位数，所以就非常容易进行分割




