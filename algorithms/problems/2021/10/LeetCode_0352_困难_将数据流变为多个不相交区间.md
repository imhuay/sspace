## 将数据流变为多个不相交区间
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E5%9B%B0%E9%9A%BE&color=red&style=flat-square)](../../../README.md#困难)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE&color=blue&style=flat-square)](../../../README.md#二分查找)
[![](https://img.shields.io/static/v1?label=&message=%E6%A8%A1%E6%8B%9F&color=blue&style=flat-square)](../../../README.md#模拟)
<!--END_SECTION:badge-->
<!--info
tags: [二分查找, 模拟]
source: LeetCode
level: 困难
number: '0352'
name: 将数据流变为多个不相交区间
companies: []
-->

<summary><b>问题描述</b></summary>

```txt
给你一个由非负整数 a1, a2, ..., an 组成的数据流输入, 请你将到目前为止看到的数字总结为不相交的区间列表.

实现 SummaryRanges 类:
    SummaryRanges() 使用一个空数据流初始化对象.
    void addNum(int val) 向数据流中加入整数 val .
    int[][] getIntervals() 以不相交区间 [starti, endi] 的列表形式返回对数据流中整数的总结.

进阶: 如果存在大量合并, 并且与数据流的大小相比, 不相交区间的数量很小, 该怎么办?

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

** "进阶" **: 在插入过程中完成合并操作;

<details><summary><b>示例</b></summary>

```txt
输入:
    ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
输出:
    [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

解释:
    SummaryRanges summaryRanges = new SummaryRanges();
    summaryRanges.addNum(1);      // arr = [1]
    summaryRanges.getIntervals(); // 返回 [[1, 1]]
    summaryRanges.addNum(3);      // arr = [1, 3]
    summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]]
    summaryRanges.addNum(7);      // arr = [1, 3, 7]
    summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]]
    summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
    summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]]
    summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
    summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]]

提示:
    0 <= val <= 10^4
    最多调用 addNum 和 getIntervals 方法 3 * 10^4 次

来源: 力扣 (LeetCode)
链接: https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals
著作权归领扣网络所有. 商业转载请联系官方授权, 非商业转载请注明出处.
```

</details>


<summary><b>思路</b></summary>

<details><summary><b>法1) Python: 暴力求解</b></summary>

- 每次 `getIntervals` 时, 先对数组排序, 然后依次找出每个不相交的区间;

```python
class SummaryRanges:

    def __init__(self):
        self.ls = []

    def addNum(self, val: int) -> None:
        """"""
        self.ls.append(val)

    def getIntervals(self) -> List[List[int]]:
        """"""
        ls = sorted(self.ls)
        ret = []
        l = ls[0]
        for i in range(1, len(ls)):
            if ls[i] - ls[i-1] > 1:  # 判断是否需要合并
                ret.append([l, ls[i-1]])
                l = ls[i]

        ret.append([l, ls[-1]])

        return ret
```

</details>


<details><summary><b>法2) Python: 模拟, 分情况讨论</b></summary>

- 明确每次 `addNum` 时, 区间会发生那些变化:
    - 情况1: 存在一个区间 `[l, r]` 满足 `l <= val <= r`;
    - 情况2: 存在一个区间 `[l, r]` 满足 `r + 1 == val`;
    - 情况3: 存在一个区间 `[l, r]` 满足 `l - 1 == val`;
    - 情况4: 存在两个个区间 `[l0, r0]` 和 `[l1, r1]` 满足 `r0 + 1 == val == l1 - 1`, 即加入 val 后, 会合并为一个区间 `[l0, r1]`
    - 情况5: 以上均不满足, 加入后 val 单独成为一个区间;

- 这里使用了 `SortedDict` 降低了代码难度, 也可以使用一个有序数组来模拟;

- 时间复杂度: `addNum O(NlgN)`、`getIntervals O(N)`;
- 空间复杂度: `O(N)`;


```python
from sortedcontainers import SortedDict
from bisect import bisect_right, bisect_left

class SummaryRanges:

    def __init__(self):
        self.ret = SortedDict()  # {l: r}
        # 加入首尾两个哨兵, 防止区间不存在的情况, 这样会徒增很多判断
        self.ret[-10] = -10
        self.ret[10010] = 10010

    def addNum(self, val: int) -> None:
        ret = self.ret
        L = list(self.ret.keys())
        R = list(self.ret.values())

        # 二分找出 val 的相邻区间
        idx = bisect_left(L, val)  # idx = ret.bisect_left(val)
        pre = L[idx - 1], R[idx - 1]
        nxt = L[idx], R[idx]

        if pre[0] <= val <= pre[1] or nxt[0] <= val <= nxt[1]:  # 情况1
            pass
        elif pre[1] + 1 == val == nxt[0] - 1:  # 情况4
            ret.pop(nxt[0])
            ret[pre[0]] = nxt[1]
        elif pre[1] + 1 == val:  # 情况2
            ret[pre[0]] = val
        elif nxt[0] - 1 == val:  # 情况3
            ret.pop(nxt[0])
            ret[val] = nxt[1]
        else:  # 情况5
            ret[val] = val

    def getIntervals(self) -> List[List[int]]:
        return list(self.ret.items())[1:-1]  # 去除两个哨兵
```

- 上面的代码中用到了 `SortedDict`, 示例:

```python
>>> d = SortedDict()
>>> d[3] = 33
>>> d[2] = 22
>>> d[4] = 44
>>> d[6] = 66
>>> d[7] = 77
>>> d
SortedDict({2: 22, 3: 33, 4: 44, 6: 66, 7: 77})
>>> d.bisect_left(4)  # 二分查找返回的是插入位置
2
>>> d.bisect_right(4)  # left 和 right 的区别是如果插入值已存在, 则 left 会插到前面, right 会插到后面
3
```

</details>


<!--START_SECTION:relate_note-->
---

### 算法笔记

> 🌧️ _暂无主题相关的笔记_


<details><summary><b>其他算法笔记</b></summary>

- [从递归到递推 (动态规划)](../../../../notes/_archives/2022/10/从暴力递归到动态规划.md)  
- [树形递归技巧](../../../../notes/_archives/2022/10/树形递归技巧.md)  
- [滑动窗口模板](../../../../notes/_archives/2022/10/滑动窗口模板.md)  
- [链表常用操作备忘](../../../../notes/_archives/2022/10/链表模板.md)  

</details>
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
---

### 相关问题


<details><summary><b>二分查找 (23)</b></summary>

> [[中等, LeetCode] 两数相除](LeetCode_0029_中等_两数相除.md)  
> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](../../2022/10/LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 搜索二维矩阵 II 🔥](../../2022/07/LeetCode_0240_中等_搜索二维矩阵II.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, 剑指Offer2] 整数除法 🔥](../../2022/09/剑指Offer2_001_中等_整数除法.md)  
> [[中等, 剑指Offer] 二维数组中的查找](../11/剑指Offer_0400_中等_二维数组中的查找.md)  
> [[中等, 剑指Offer] 数值的整数次方 (快速幂) 🔥](../11/剑指Offer_1600_中等_数值的整数次方(快速幂).md)  
> [[中等, 牛客] 二分查找-II](../../2022/04/牛客_0105_中等_二分查找-II.md)  
> [[中等, 牛客] 二维数组中的查找](../../2022/02/牛客_0029_中等_二维数组中的查找.md)  
> [[中等, 牛客] 寻找峰值 🔥](../../2022/04/牛客_0107_中等_寻找峰值.md)  
> [[中等, 牛客] 矩阵元素查找](../../2022/04/牛客_0086_中等_矩阵元素查找.md)  
  > 
> [[困难, LeetCode] 寻找两个正序数组的中位数 🔥](../../2022/02/LeetCode_0004_困难_寻找两个正序数组的中位数.md)  
> [[困难, 牛客] 在两个长度相等的排序数组中找到上中位数](../../2022/02/牛客_0036_困难_在两个长度相等的排序数组中找到上中位数.md)  
  > 
> [[简单, LeetCode] x 的平方根 🔥](../../2022/10/LeetCode_0069_简单_x的平方根.md)  
> [[简单, LeetCode] 排列硬币](LeetCode_0441_简单_排列硬币.md)  
> [[简单, 剑指Offer2] 山峰数组的顶部](../../2022/09/剑指Offer2_069_简单_山峰数组的顶部.md)  
> [[简单, 剑指Offer] 在排序数组中查找数字](../../2022/01/剑指Offer_5302_简单_在排序数组中查找数字.md)  
> [[简单, 剑指Offer] 旋转数组的最小数字](../11/剑指Offer_1100_简单_旋转数组的最小数字.md)  
> [[简单, 剑指Offer] 求0～n-1中缺失的数字](../../2022/01/剑指Offer_5301_简单_求0～n-1中缺失的数字.md)  
> [[简单, 牛客] 在旋转过的有序数组中寻找目标值](../../2022/03/牛客_0048_简单_在旋转过的有序数组中寻找目标值.md)  
> [[简单, 牛客] 数字在升序数组中出现的次数](../../2022/03/牛客_0074_简单_数字在升序数组中出现的次数.md)  
> [[简单, 牛客] 旋转数组的最小数字](../../2022/03/牛客_0071_简单_旋转数组的最小数字.md)  
> [[简单, 牛客] 求平方根 🔥](../../2022/02/牛客_0032_简单_求平方根.md)  
  > 

</details>

<details><summary><b>模拟 (15)</b></summary>

> [[中等, LeetCode] 分割数组](../../2022/06/LeetCode_0915_中等_分割数组.md)  
> [[中等, 剑指Offer] 买卖股票的最佳时机](../../2022/01/剑指Offer_6300_中等_买卖股票的最佳时机.md)  
> [[中等, 剑指Offer] 圆圈中最后剩下的数字 (约瑟夫环问题) 🔥](../../2022/01/剑指Offer_6200_中等_圆圈中最后剩下的数字(约瑟夫环问题).md)  
> [[中等, 牛客] 大数乘法](../../2022/01/牛客_0010_中等_大数乘法.md)  
> [[中等, 牛客] 大数加法](../../2022/01/牛客_0001_中等_大数加法.md)  
> [[中等, 牛客] 最长回文子串](../../2022/01/牛客_0017_中等_最长回文子串.md)  
> [[中等, 牛客] 螺旋矩阵](../../2022/03/牛客_0038_中等_螺旋矩阵.md)  
  > 
> [[简单, LeetCode] 亲密字符串](../11/LeetCode_0859_简单_亲密字符串.md)  
> [[简单, 剑指Offer] 扑克牌中的顺子](../../2022/01/剑指Offer_6100_简单_扑克牌中的顺子.md)  
> [[简单, 剑指Offer] 数组中出现次数超过一半的数字 (摩尔投票) 🔥](../12/剑指Offer_3900_简单_数组中出现次数超过一半的数字(摩尔投票).md)  
> [[简单, 牛客] 买卖股票的最好时机(一)](../../2022/01/牛客_0007_简单_买卖股票的最好时机(一).md)  
> [[简单, 牛客] 反转数字](../../2022/03/牛客_0057_简单_反转数字.md)  
> [[简单, 牛客] 字符串变形](../../2022/04/牛客_0089_简单_字符串变形.md)  
> [[简单, 牛客] 扑克牌顺子](../../2022/03/牛客_0063_简单_扑克牌顺子.md)  
> [[简单, 牛客] 数组中出现次数超过一半的数字](../../2022/03/牛客_0073_简单_数组中出现次数超过一半的数字.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
