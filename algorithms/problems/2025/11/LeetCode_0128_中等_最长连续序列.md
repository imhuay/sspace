## 最长连续序列
<!--START_SECTION:badge-->
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-11-11%2013%3A04%3A08&labelColor=gray&color=thistle&style=flat-square)
[![](https://img.shields.io/static/v1?label=&message=%E4%B8%AD%E7%AD%89&color=yellow&style=flat-square)](../../../README.md#中等)
[![](https://img.shields.io/static/v1?label=&message=LeetCode&color=darkcyan&style=flat-square)](../../../README.md#leetcode)
[![](https://img.shields.io/static/v1?label=&message=LeetCode%20Hot%20100&color=blue&style=flat-square)](../../../README.md#leetcode-hot-100)
[![](https://img.shields.io/static/v1?label=&message=%E5%8C%BA%E9%97%B4%E5%90%88%E5%B9%B6&color=blue&style=flat-square)](../../../README.md#区间合并)
[![](https://img.shields.io/static/v1?label=&message=%E5%93%88%E5%B8%8C%E8%A1%A8%28Hash%29&color=blue&style=flat-square)](../../../README.md#哈希表hash)
<!--END_SECTION:badge-->
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [哈希表, 区间合并, lc100]
source: LeetCode
level: 中等
number: '128'
name: '最长连续序列'
-->

> [128. 最长连续序列 - 力扣 (LeetCode) ](https://leetcode.cn/problems/longest-consecutive-sequence/)

<summary><b>问题简述</b></summary>

```txt
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
```

<!-- 
<details><summary><b>详细描述</b></summary>

```txt
```

</details>
-->

<!-- <div align='center'><img src='../../../_assets/xxx.png' height='300' /></div> -->

---

<summary><b>思路 1: 哈希集合/遍历</b></summary>

- 逐一遍历每个元素会产生很多冗余工作, 实际上我们无需一次针对每个元素 `x` 去判断 `x+1`, `x+2`, ... 是否在数组中
- 如果 `x-1` 已经在数组中, 那么 `x-1` 肯定会进行相应的遍历, 然后遍历到 `x`, 而且从 `x-1` 开始的遍历必定比从 `x` 开始的得到的序列更长
- 因此, 可将在一个连续序列中的元素进行删减, 让其只在最小的元素才开始遍历

<details><summary><b>Python</b></summary>

```python
def longestConsecutive(self, nums: List[int]) -> int:
    st = set(nums)
    ans = 0

    for x in st:
        if x - 1 in st:
            continue
        
        y = x + 1
        while y in st:
            y += 1
        
        ans = max(ans, y - x)

    return ans
```

</details>

---

<summary><b>思路 2: 哈希表/区间合并</b></summary>

- 定义哈希表 `mp[i] = l` 表示: **如果 `i` 作为某个连续区间的边界, 则该区间的长度为 `l`**
    - 插入一个新数 x 时, 检查它左边和右边的区间长度
    - 把它和左右区间合并成一个更大的区间
    - 更新新区间的左右边界长度
- **示例**
    ```md
    输入：`nums = [100, 4, 200, 1, 3, 2]`

    1. 插入 `100` → 左右都没有 → 区间长度 1 → mp[100]=1
    2. 插入 `4` → 左右都没有 → 区间长度 1 → mp[4]=1
    3. 插入 `200` → 区间长度 1 → mp[200]=1
    4. 插入 `1` → 区间长度 1 → mp[1]=1
    5. 插入 `3` → 左边有 `2` 吗？没有；右边有 `4` 吗？有，长度 1 → 合并成长度 2 → mp[3]=2, mp[4]=2
    6. 插入 `2` → 左边有 `1` 长度 1，右边有 `3` 长度 2 → 合并成长度 4 → mp[1]=4, mp[4]=4

    最终答案 ret=4，对应序列 `[1,2,3,4]`。
    ```

<details><summary><b>Python</b></summary>

```python
def longestConsecutive(self, nums: List[int]) -> int:
    used = set()   # 记录已经处理过的数字
    mp = dict()    # 哈希表, mp[i] = l 表示 i 作为边界能提供的区间长度
    ans = 0        # 最终答案: 最长连续序列长度

    for x in nums:
        if x not in used:          # 避免重复处理同一个数
            used.add(x)

            # 查看 x 左边和右边的连续长度
            l = mp.get(x - 1, 0)   # 左边连续长度
            r = mp.get(x + 1, 0)   # 右边连续长度

            # 当前数 x 加上左右两边的长度，形成新的区间长度
            mx = l + 1 + r

            # 更新区间的边界长度：
            # mp[x - l] 是新区间的左边界
            # mp[x + r] 是新区间的右边界
            mp[x - l] = mp[x + r] = mx

            # 更新答案
            ans = max(ans, mx)

    return ans
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


<details><summary><b>LeetCode Hot 100 (32)</b></summary>

> [[中等, LeetCode] 三数之和 🔥](../../2021/10/LeetCode_0015_中等_三数之和.md)  
> [[中等, LeetCode] 下一个排列 🔥](../../2022/10/LeetCode_0031_中等_下一个排列.md)  
> [[中等, LeetCode] 两数相加 🔥](../../2021/10/LeetCode_0002_中等_两数相加.md)  
> [[中等, LeetCode] 全排列 🔥](../../2022/10/LeetCode_0046_中等_全排列.md)  
> [[中等, LeetCode] 全排列II 🔥](../../2022/10/LeetCode_0047_中等_全排列II.md)  
> [[中等, LeetCode] 删除链表的倒数第N个结点 🔥](../../2022/01/LeetCode_0019_中等_删除链表的倒数第N个结点.md)  
> [[中等, LeetCode] 和为K的子数组 🔥](LeetCode_0560_中等_和为K的子数组.md)  
> [[中等, LeetCode] 在排序数组中查找元素的第一个和最后一个位置 🔥](../../2022/10/LeetCode_0034_中等_在排序数组中查找元素的第一个和最后一个位置.md)  
> [[中等, LeetCode] 字母异位词分组 🔥](../../2022/10/LeetCode_0049_中等_字母异位词分组.md)  
> [[中等, LeetCode] 找到字符串中所有字母异位词 🔥](LeetCode_0438_中等_找到字符串中所有字母异位词.md)  
> [[中等, LeetCode] 括号生成 🔥](../../2022/10/LeetCode_0022_中等_括号生成.md)  
> [[中等, LeetCode] 搜索旋转排序数组 🔥](../../2021/10/LeetCode_0033_中等_搜索旋转排序数组.md)  
> [[中等, LeetCode] 数组中的第K个最大元素 🔥](../../2022/10/LeetCode_0215_中等_数组中的第K个最大元素.md)  
> [[中等, LeetCode] 无重复字符的最长子串 🔥](../../2022/02/LeetCode_0003_中等_无重复字符的最长子串.md)  
> [[中等, LeetCode] 最长回文子串 🔥](../../2021/10/LeetCode_0005_中等_最长回文子串.md)  
> [[中等, LeetCode] 电话号码的字母组合 🔥](../../2022/10/LeetCode_0017_中等_电话号码的字母组合.md)  
> [[中等, LeetCode] 盛最多水的容器 🔥](../../2021/10/LeetCode_0011_中等_盛最多水的容器.md)  
> [[中等, LeetCode] 组合总和 II 🔥](../../2022/10/LeetCode_0040_中等_组合总和II.md)  
> [[中等, LeetCode] 组合总和 🔥](../../2022/10/LeetCode_0039_中等_组合总和.md)  
  > 
> [[困难, LeetCode] K个一组翻转链表 🔥](../../2022/02/LeetCode_0025_困难_K个一组翻转链表.md)  
> [[困难, LeetCode] 合并K个升序链表 🔥](../../2022/10/LeetCode_0023_困难_合并K个升序链表.md)  
> [[困难, LeetCode] 寻找两个正序数组的中位数 🔥](../../2022/02/LeetCode_0004_困难_寻找两个正序数组的中位数.md)  
> [[困难, LeetCode] 接雨水 🔥](../../2021/10/LeetCode_0042_困难_接雨水.md)  
> [[困难, LeetCode] 最小覆盖子串 🔥](LeetCode_0076_困难_最小覆盖子串.md)  
> [[困难, LeetCode] 最长有效括号 🔥](../../2022/10/LeetCode_0032_困难_最长有效括号.md)  
> [[困难, LeetCode] 正则表达式匹配 🔥](../../2022/01/LeetCode_0010_困难_正则表达式匹配.md)  
> [[困难, LeetCode] 滑动窗口最大值 🔥](../../2022/10/LeetCode_0239_困难_滑动窗口最大值.md)  
> [[困难, 牛客] 最小覆盖子串 🔥](../../2022/02/牛客_0028_困难_最小覆盖子串.md)  
  > 
> [[简单, LeetCode] 两数之和 🔥](../../2021/10/LeetCode_0001_简单_两数之和.md)  
> [[简单, LeetCode] 合并两个有序链表 🔥](../../2021/10/LeetCode_0021_简单_合并两个有序链表.md)  
> [[简单, LeetCode] 有效的括号 🔥](../../2022/03/LeetCode_0020_简单_有效的括号.md)  
> [[简单, LeetCode] 移动零 🔥](LeetCode_0283_简单_移动零.md)  
  > 

</details>

<details><summary><b>哈希表(Hash) (12)</b></summary>

> [[中等, LeetCode] 字母异位词分组 🔥](../../2022/10/LeetCode_0049_中等_字母异位词分组.md)  
> [[中等, LeetCode] 重复的DNA序列](../../2022/07/LeetCode_0187_中等_重复的DNA序列.md)  
> [[中等, 剑指Offer] 复杂链表的复制 (深拷贝) 🔥](../../2021/12/剑指Offer_3500_中等_复杂链表的复制(深拷贝).md)  
> [[中等, 剑指Offer] 最长不含重复字符的子字符串](../../2021/12/剑指Offer_4800_中等_最长不含重复字符的子字符串.md)  
> [[中等, 牛客] 和为K的连续子数组](../../2022/05/牛客_0125_中等_和为K的连续子数组.md)  
  > 
> [[困难, 牛客] 数组中的最长连续子序列](../../2022/04/牛客_0095_困难_数组中的最长连续子序列.md)  
  > 
> [[简单, LeetCode] 两数之和 🔥](../../2021/10/LeetCode_0001_简单_两数之和.md)  
> [[简单, 剑指Offer] 数组中重复的数字](../../2021/11/剑指Offer_0300_简单_数组中重复的数字.md)  
> [[简单, 剑指Offer] 第一个只出现一次的字符](../../2021/12/剑指Offer_5000_简单_第一个只出现一次的字符.md)  
> [[简单, 牛客] 两数之和](../../2022/03/牛客_0061_简单_两数之和.md)  
> [[简单, 牛客] 第一个只出现一次的字符](../../2022/02/牛客_0031_简单_第一个只出现一次的字符.md)  
> [[简单, 程序员面试金典] 判定是否互为字符重排](../../2022/09/程序员面试金典_0102_简单_判定是否互为字符重排.md)  
  > 

</details>
<!--END_SECTION:relate_problem-->
