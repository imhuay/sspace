## 重复的DNA序列
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E4%BD%8D%E8%BF%90%E7%AE%97&color=blue&style=flat-square)](../../../README.md#位运算)
[![](https://img.shields.io/static/v1?label=&message=%E5%93%88%E5%B8%8C%E8%A1%A8%28Hash%29&color=blue&style=flat-square)](../../../README.md#哈希表hash)
<!--END_SECTION:badge-->
<!--info
tags: [哈希表, 位运算]
source: LeetCode
level: 中等
number: '0187'
name: 重复的DNA序列
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
找出由 ATCG 构成的字符串中所有重复且长度为 10 的子串;
```

<details><summary><b>详细描述</b></summary>

```txt
所有 DNA 都由一系列缩写为 'A', 'C', 'G' 和 'T' 的核苷酸组成, 例如: "ACGAATTCCG". 在研究 DNA 时, 识别 DNA 中的重复序列有时会对研究非常有帮助.

编写一个函数来找出所有目标子串, 目标子串的长度为 10, 且在 DNA 字符串 s 中出现次数超过一次.

示例 1:
    输入: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    输出: ["AAAAACCCCC","CCCCCAAAAA"]
示例 2:
    输入: s = "AAAAAAAAAAAAA"
    输出: ["AAAAAAAAAA"]

提示:
    0 <= s.length <= 10^5
    s[i] 为 'A'、'C'、'G' 或 'T'

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/repeated-dna-sequences
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<summary><b>思路</b></summary>

- 基本思路: 哈希表计数;
- 如果直接使用子串本身作为哈希表的 key, 那么时间复杂度和空间复杂度都是 `O(NL)`; 而如果使用位运算+滑动窗口手动构造 key, 可以把复杂度降为 `O(N)`;


<details><summary><b>子串作为 key</b></summary>

- 时间&空间复杂度: `O(NL)`;
```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """"""
        # from collections import defaultdict
        L = 10

        cnt = defaultdict(int)
        ans = []
        for i in range(len(s) - L + 1):
            subs = s[i: i+L]
            cnt[subs] += 1
            if cnt[subs] == 2:
                ans.append(subs)

        return ans
```

</details>

<details><summary><b>位运算+滑动窗口</b></summary>

- 时间&空间复杂度: `O(N)`;
```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """"""
        # from collections import defaultdict
        L = 10
        B = {'A': 0, 'T': 1, 'C': 2, 'G': 3}  # 分别为 00, 01, 10, 11

        if len(s) < L + 1:  # assert, 否则部分用例会无法通过
            return []

        # 先计算前 9 位的值
        x = 0
        for i in range(L - 1):
            b = B[s[i]]
            x = (x << 2) | b

        ans = []
        cnt = defaultdict(int)
        for i in range(len(s) - L + 1):
            b = B[s[i + L - 1]]
            # 注意该有的括号不要少, 避免运算优先级混乱
            x = ((x << 2) | b) & ((1 << (L * 2)) - 1)  # 滑动计算子串的 hash 值
            cnt[x] += 1
            if cnt[x] == 2:
                ans.append(s[i: i + L])

        return ans
```

</details>


<details><summary><b>位运算说明</b></summary>

- `(x << 2) | b`:
    ```python
    # 以为均为二进制表示
    设 x = 0010 1011, b = 10:
    该运算相当于把 b "拼" 到 x 末尾

    x         :   0010 1011
    x = x << 2:   1010 1100

    x = x | b :   1010 1100
                | 0000 0010
                -----------
                  1010 1110
    ```
- `x & ((1 << (L * 2)) - 1)`
    ```python
    # 该运算把 x 除低 10 位前的所有位置置 0
    设 L = 5, x = 1110 1010 1010:

    y = 1 << (L * 2):   0100 0000 0000
    y = y - 1       :   0011 1111 1111

    x = x & y       :   1110 1010 1010
                      & 0011 1111 1111
                      ----------------
                        0010 1010 1010

    ```

</details>


<!--START_SECTION:relate_note-->
---

### 算法笔记

> 🌧️ _暂无主题相关的笔记_


<details><summary><b>其他算法笔记</b></summary>

- [二分查找相关](../../../../notes/_archives/2025/10/二分查找备忘.md)  
- [从递归到递推 (动态规划)](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  
- [链表操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>位运算 (8)</b></summary>

> [[中等, LeetCode] 两数相除](../../2021/10/LeetCode_0029_中等_两数相除.md)  
> [[中等, 剑指Offer] 数组中数字出现的次数](../01/剑指Offer_5601_中等_数组中数字出现的次数.md)  
> [[中等, 剑指Offer] 数组中数字出现的次数](../01/剑指Offer_5602_中等_数组中数字出现的次数.md)  
> [[中等, 牛客] 数组中只出现一次的两个数字 🔥](../03/牛客_0075_中等_数组中只出现一次的两个数字.md)  
  > 
> [[困难, 牛客] N皇后问题](../03/牛客_0039_困难_N皇后问题.md)  
  > 
> [[简单, 剑指Offer] 不用加减乘除做加法](../01/剑指Offer_6500_简单_不用加减乘除做加法.md)  
> [[简单, 剑指Offer] 二进制中1的个数](../../2021/11/剑指Offer_1500_简单_二进制中1的个数.md)  
> [[简单, 牛客] 二进制中1的个数 🔥](../05/牛客_0120_简单_二进制中1的个数.md)  
  > 

</details>

<details><summary><b>哈希表(Hash) (11)</b></summary>

> [[中等, LeetCode] 字母异位词分组 🔥](../10/LeetCode_0049_中等_字母异位词分组.md)  
> [[中等, 剑指Offer] 复杂链表的复制 (深拷贝) 🔥](../../2021/12/剑指Offer_3500_中等_复杂链表的复制(深拷贝).md)  
> [[中等, 剑指Offer] 最长不含重复字符的子字符串](../../2021/12/剑指Offer_4800_中等_最长不含重复字符的子字符串.md)  
> [[中等, 牛客] 和为K的连续子数组](../05/牛客_0125_中等_和为K的连续子数组.md)  
  > 
> [[困难, 牛客] 数组中的最长连续子序列](../04/牛客_0095_困难_数组中的最长连续子序列.md)  
  > 
> [[简单, LeetCode] 两数之和 🔥](../../2021/10/LeetCode_0001_简单_两数之和.md)  
> [[简单, 剑指Offer] 数组中重复的数字](../../2021/11/剑指Offer_0300_简单_数组中重复的数字.md)  
> [[简单, 剑指Offer] 第一个只出现一次的字符](../../2021/12/剑指Offer_5000_简单_第一个只出现一次的字符.md)  
> [[简单, 牛客] 两数之和](../03/牛客_0061_简单_两数之和.md)  
> [[简单, 牛客] 第一个只出现一次的字符](../02/牛客_0031_简单_第一个只出现一次的字符.md)  
> [[简单, 程序员面试金典] 判定是否互为字符重排](../09/程序员面试金典_0102_简单_判定是否互为字符重排.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
