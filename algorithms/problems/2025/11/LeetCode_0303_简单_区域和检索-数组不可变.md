## <title - autoUpdate>
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
tags: [前缀和]
source: 'LeetCode'
level: '简单'
number: '303'
name: '区域和检索 - 数组不可变'
-->

> [303. 区域和检索 - 数组不可变 - 力扣（LeetCode）](https://leetcode.cn/problems/range-sum-query-immutable/)

<summary><b>问题简述</b></summary>

```md
给定一个整数数组  nums，处理以下类型的多个查询:

计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right

实现 NumArray 类：

NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，包含 left 和 right 两点( 也就是 nums[left] + nums[left + 1] + ... + nums[right] )
```

<!-- 
<details><summary><b>详细描述</b></summary>

```md
```

</details>
-->

<!-- <div align='center'><img src='../../../_assets/xxx.png' height='300' /></div> -->

---

<summary><b>思路</b></summary>

- 前缀和模板

<details><summary><b>Python</b></summary>

```python
class NumArray:
    def __init__(self, nums: List[int]):
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x
        self.s = s

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]
```

</details>


<!--START_SECTION:relate_note-->
<!--END_SECTION:relate_note-->


<!--START_SECTION:relate_problem-->
<!--END_SECTION:relate_problem-->