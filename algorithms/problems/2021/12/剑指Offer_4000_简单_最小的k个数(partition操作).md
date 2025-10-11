## 最小的k个数 (partition操作)
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-09-23%2002%3A03%3A22&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E7%AE%80%E5%8D%95&color=yellow&style=flat-square)](../../../README.md#简单)
[![](https://img.shields.io/static/v1?label=&message=%E5%89%91%E6%8C%87Offer&color=green&style=flat-square)](../../../README.md#剑指offer)
[![](https://img.shields.io/static/v1?label=&message=%E5%A0%86/%E4%BC%98%E5%85%88%E9%98%9F%E5%88%97&color=blue&style=flat-square)](../../../README.md#堆优先队列)
[![](https://img.shields.io/static/v1?label=&message=%E6%8E%92%E5%BA%8F&color=blue&style=flat-square)](../../../README.md#排序)
[![](https://img.shields.io/static/v1?label=&message=%E7%BB%8F%E5%85%B8&color=blue&style=flat-square)](../../../README.md#经典)
<!--END_SECTION:badge-->
<!--info
tags: [优先队列, 快排, 经典]
source: 剑指Offer
level: 简单
number: '4000'
name: 最小的k个数 (partition操作)
companies: []
-->

<summary><b>问题简述</b></summary>

```txt
输入整数数组 arr , 找出其中最小的 k 个数
```
> [剑指 Offer 40. 最小的k个数 - 力扣 (LeetCode) ](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)

<details><summary><b>详细描述</b></summary>

```txt
输入整数数组 arr , 找出其中最小的 k 个数. 例如, 输入4、5、1、6、2、7、3、8这8个数字, 则最小的4个数字是1、2、3、4.

示例 1:
    输入: arr = [3,2,1], k = 2
    输出: [1,2] 或者 [2,1]
示例 2:
    输入: arr = [0,1,2,1], k = 1
    输出: [0]

限制:
    0 <= k <= arr.length <= 10000
    0 <= arr[i] <= 10000

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路1: 快排中的 partition 过程</b></summary>

- 快排的过程:
    - **partition 过程**: 以数组某个元素 (一般取首元素) 为基准数, 将所有小于基准数的元素移动至其左边, 大于基准数的元素移动至其右边.
    - 递归地对左右部分执行 **partition 过程**, 直至区域内的元素数量为 1;
- 基于以上思想, 当某次划分后基准数正好是第 k+1 小的数字, 那么此时基准数左边的所有数字便是题目要求的最小的 k 个数.

<details><summary><b>Python</b></summary>

```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        def partition(lo, hi):  # [lo, hi]
            if lo >= hi: return

            p = arr[lo]  # 选取第一个位置为基准点
            l, r = lo, hi  # l 的初始位置应该在 lo, 而不是 lo + 1
            # 假设初始化为 lo + 1, 当 a[lo] 为最小值时, 此时训处循环后 l == r == lo + 1, 再交换 a[lo] 和 a[l] 就会出错

            while l < r:  # 退出循环时 l == r
                # 先移动 r, 在移动 l, 此时退出循环后 l 和 r 同时指向一个小于 p 的值; 反之, 如果用 a[hi] 初始化 p, 就要先移动 l, 在移动 r;

                # 从 r 开始, 从右往左找到第一个 < p 的值, 所以循环条件是 >=
                while l < r and arr[r] >= p: r -= 1
                # 从 l 开始, 从左往右找到第一个 > p 的值, 所以循环条件是 <=
                while l < r and arr[l] <= p: l += 1
                arr[l], arr[r] = arr[r], arr[l]

            arr[lo], arr[l] = arr[l], arr[lo]  # 将基准点移动到分界点

            if l < k: partition(l + 1, hi)
            if l > k: partition(lo, l - 1)

        partition(0, len(arr) - 1)
        return arr[:k]
```

</details>


<summary><b>思路2: 堆 (优先队列) </b></summary>

- **写法1) ** 维护一个长度为 k 的大顶堆 (第一个数最大), 当下一个元素小于堆顶值, 就更新堆 (弹出堆顶, 插入新值);
- **写法2) ** 直接对整个数组构建一个小顶堆, 然后循环弹出前 k 个值;
- 注意写法1 的时间复杂度是 `O(NlogK)`, 而写法2 是 `O(NlogN)`;

<details><summary><b>Python: 写法1 (使用库函数) </b></summary>

```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k < 1 or not arr:  # 使用堆, 要添加非空断言
            return []

        import heapq

        # python 默认是小顶堆, 且不支持自定义比较函数, 所以要添加负号转成取前 k 大的数
        ret = [-x for x in arr[:k]]
        heapq.heapify(ret)

        for i in range(k, len(arr)):
            if -arr[i] > ret[0]:
                heapq.heappop(ret)
                heapq.heappush(ret, -arr[i])

        return [-x for x in ret]
```

</details>

<details><summary><b>Python: 写法2 (使用库函数) </b></summary>

```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k < 1 or not arr:  # 使用堆, 要添加非空断言
            return []

        import heapq

        # python 默认是小顶堆
        heapq.heapify(arr)

        ret = []
        for _ in range(k):
            ret.append(heapq.heappop(arr))

        return ret
```

</details>


<summary><b>思路3: 计数排序</b></summary>

- 因为题目限制了 `arr[i]` 的范围, 所以还可以使用计数排序, 时间复杂度 `O(N)`;

<details><summary><b>Python</b></summary>

```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k >= len(arr):  # 使用计数排序要加长度判断
            return arr

        dp = [0] * 10001

        for x in arr:
            dp[x] += 1

        ret = []
        cnt = 0
        for i in range(len(dp)):
            while dp[i] and cnt < k:
                ret.append(i)
                cnt += 1
                dp[i] -= 1
            if cnt == k:
                return ret
```

</details>


<!--START_SECTION:relate_problem-->
---

### 相关主题

<details><summary><b>堆/优先队列</b></summary>

> [[中等, 剑指Offer2] 数组中的第K大的数字](../../2022/09/剑指Offer2_076_中等_数组中的第K大的数字.md)  
> [[中等, 牛客] 字符串出现次数的TopK问题](../../2022/04/牛客_0097_中等_字符串出现次数的TopK问题.md)  
  > 
> [[困难, LeetCode] 合并K个升序链表 🔥](../../2022/10/LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 滑动窗口最大值 🔥](../../2022/10/LeetCode_0239_困难_滑动窗口最大值.md)  
> [[困难, 剑指Offer] 数据流中的中位数](剑指Offer_4100_困难_数据流中的中位数.md)  
> [[困难, 牛客] 合并k个已排序的链表](../../2022/03/牛客_0051_困难_合并k个已排序的链表.md)  
> [[困难, 牛客] 滑动窗口的最大值](../../2022/03/牛客_0082_困难_滑动窗口的最大值.md)  
  > 
> [[简单, 牛客] 三个数的最大乘积](../../2022/04/牛客_0106_简单_三个数的最大乘积.md)  
  > 

</details>
<details><summary><b>排序</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 数组中的第K个最大元素 🔥](../../2022/10/LeetCode_0215_中等_数组中的第K个最大元素.md)  
> [[中等, 剑指Offer2] 数组中的第K大的数字](../../2022/09/剑指Offer2_076_中等_数组中的第K大的数字.md)  
> [[中等, 剑指Offer] 把数组排成最小的数](剑指Offer_4500_中等_把数组排成最小的数.md)  
> [[中等, 牛客] 合并区间](../../2022/02/牛客_0037_中等_合并区间.md)  
> [[中等, 牛客] 字符串出现次数的TopK问题](../../2022/04/牛客_0097_中等_字符串出现次数的TopK问题.md)  
> [[中等, 牛客] 寻找第K大](../../2022/04/牛客_0088_中等_寻找第K大.md)  
> [[中等, 牛客] 拼接所有的字符串产生字典序最小的字符串](../../2022/04/牛客_0085_中等_拼接所有的字符串产生字典序最小的字符串.md)  
> [[中等, 牛客] 数组中的逆序对](../../2022/05/牛客_0118_中等_数组中的逆序对.md)  
> [[中等, 牛客] 最大数](../../2022/04/牛客_0111_中等_最大数.md)  
> [[中等, 牛客] 最小的K个数](../../2022/05/牛客_0119_中等_最小的K个数.md)  
  > 
> [[简单, 剑指Offer] 扑克牌中的顺子](../../2022/01/剑指Offer_6100_简单_扑克牌中的顺子.md)  
> [[简单, 剑指Offer] 数组中出现次数超过一半的数字 (摩尔投票) 🔥](剑指Offer_3900_简单_数组中出现次数超过一半的数字(摩尔投票).md)  
> [[简单, 牛客] 三个数的最大乘积](../../2022/04/牛客_0106_简单_三个数的最大乘积.md)  
> [[简单, 程序员面试金典] 判定字符是否唯一](../../2022/09/程序员面试金典_0101_简单_判定字符是否唯一.md)  
  > 

</details>
<details><summary><b>经典</b></summary>

> [[中等, LeetCode] 下一个排列 🔥](../../2022/10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 二叉树的完全性检验 🔥](../../2022/03/LeetCode_0958_中等_二叉树的完全性检验.md)  
> [[中等, LeetCode] 最长递增子序列 🔥](../../2022/06/LeetCode_0300_中等_最长递增子序列.md)  
> [[中等, 剑指Offer2] 整数除法 🔥](../../2022/09/剑指Offer2_001_中等_整数除法.md)  
> [[中等, 剑指Offer] 丑数 🔥](剑指Offer_4900_中等_丑数.md)  
> [[中等, 剑指Offer] 二叉搜索树与双向链表 🔥](剑指Offer_3600_中等_二叉搜索树与双向链表.md)  
> [[中等, 剑指Offer] 圆圈中最后剩下的数字 (约瑟夫环问题) 🔥](../../2022/01/剑指Offer_6200_中等_圆圈中最后剩下的数字(约瑟夫环问题).md)  
> [[中等, 剑指Offer] 复杂链表的复制 (深拷贝) 🔥](剑指Offer_3500_中等_复杂链表的复制(深拷贝).md)  
> [[中等, 剑指Offer] 字符串的排列 (全排列) 🔥](剑指Offer_3800_中等_字符串的排列(全排列).md)  
> [[中等, 剑指Offer] 把字符串转换成整数 🔥](../../2022/01/剑指Offer_6700_中等_把字符串转换成整数.md)  
> [[中等, 剑指Offer] 数值的整数次方 (快速幂) 🔥](../11/剑指Offer_1600_中等_数值的整数次方(快速幂).md)  
> [[中等, 剑指Offer] 栈的压入、弹出序列 🔥](../11/剑指Offer_3100_中等_栈的压入、弹出序列.md)  
> [[中等, 剑指Offer] 重建二叉树 🔥](../11/剑指Offer_0700_中等_重建二叉树.md)  
> [[中等, 剑指Offer] 顺时针打印矩阵 (3种思路4个写法) 🔥](../11/剑指Offer_2900_中等_顺时针打印矩阵(3种思路4个写法).md)  
> [[中等, 牛客] 01背包 🔥](../../2022/05/牛客_0145_中等_01背包.md)  
> [[中等, 牛客] 丢棋子问题 (鹰蛋问题) 🔥](../../2022/04/牛客_0087_中等_丢棋子问题(鹰蛋问题).md)  
> [[中等, 牛客] 字符串的排列 🔥](../../2022/05/牛客_0121_中等_字符串的排列.md)  
> [[中等, 牛客] 寻找峰值 🔥](../../2022/04/牛客_0107_中等_寻找峰值.md)  
> [[中等, 牛客] 岛屿数量 🔥](../../2022/04/牛客_0109_中等_岛屿数量.md)  
> [[中等, 牛客] 把字符串转换成整数(atoi) 🔥](../../2022/04/牛客_0100_中等_把字符串转换成整数(atoi).md)  
> [[中等, 牛客] 数组中只出现一次的两个数字 🔥](../../2022/03/牛客_0075_中等_数组中只出现一次的两个数字.md)  
> [[中等, 牛客] 最长公共子序列(二) 🔥](../../2022/04/牛客_0092_中等_最长公共子序列(二).md)  
> [[中等, 牛客] 栈和排序 🔥](../../2022/05/牛客_0115_中等_栈和排序.md)  
> [[中等, 牛客] 汉诺塔问题 🔥](../../2022/03/牛客_0067_中等_汉诺塔问题.md)  
  > 
> [[困难, LeetCode] 编辑距离 🔥](../../2022/06/LeetCode_0072_困难_编辑距离.md)  
> [[困难, 剑指Offer] 数组中的逆序对 🔥](../../2022/01/剑指Offer_5100_困难_数组中的逆序对.md)  
> [[困难, 牛客] 接雨水问题 🔥](../../2022/05/牛客_0128_困难_接雨水问题.md)  
> [[困难, 牛客] 设计LFU缓存结构 🔥](../../2022/04/牛客_0094_困难_设计LFU缓存结构.md)  
> [[困难, 牛客] 设计LRU缓存结构 🔥](../../2022/04/牛客_0093_困难_设计LRU缓存结构.md)  
  > 
> [[简单, LeetCode] 二叉树的最大深度 🔥](../../2022/07/LeetCode_0104_简单_二叉树的最大深度.md)  
> [[简单, LeetCode] 反转链表 🔥](../../2022/10/LeetCode_0206_简单_反转链表.md)  
> [[简单, 剑指Offer] 二叉搜索树的最近公共祖先 🔥](../../2022/01/剑指Offer_6801_简单_二叉搜索树的最近公共祖先.md)  
> [[简单, 剑指Offer] 反转链表 🔥](../11/剑指Offer_2400_简单_反转链表.md)  
> [[简单, 剑指Offer] 数组中出现次数超过一半的数字 (摩尔投票) 🔥](剑指Offer_3900_简单_数组中出现次数超过一半的数字(摩尔投票).md)  
> [[简单, 牛客] 二进制中1的个数 🔥](../../2022/05/牛客_0120_简单_二进制中1的个数.md)  
> [[简单, 牛客] 单链表的排序 🔥](../../2022/03/牛客_0070_简单_单链表的排序.md)  
> [[简单, 牛客] 求平方根 🔥](../../2022/02/牛客_0032_简单_求平方根.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
