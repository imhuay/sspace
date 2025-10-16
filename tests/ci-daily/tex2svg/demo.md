测试_tex2svg
===
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
date: 2025-10-15 23:15:29
toc_title: '测试_tex2svg'
top: false
draft: false
thorough: false
hidden_in_recent: true
section_number: false
omit_in_tag_toc: true
apply_tex2svg: true
level: 0
tags: []
algo_tags: []
-->

<!--START_SECTION:keywords-->
> ***Keywords**: 测试_tex2svg*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [支持的示例](#支持的示例)
- [不应该被识别的示例](#不应该被识别的示例)
<!--END_SECTION:toc-->

---

### 支持的示例

1. 单行
<div align='center'><a href='_formulas/demo/f_001.js.tex'><img src='_formulas/demo/f_001.svg'/></a></div>

2. 多行 (存在缩进)
    <div align='center'><a href='_formulas/demo/f_002.js.tex'><img src='_formulas/demo/f_002.svg'/></a></div>

3. 删除

4. 在引用中, 单行
> <div align='center'><a href='_formulas/demo/f_003.js.tex'><img src='_formulas/demo/f_003.svg'/></a></div>

5. 在引用中, 多行
> <div align='center'><a href='_formulas/demo/f_004.js.tex'><img src='_formulas/demo/f_004.svg'/></a></div>

6. 多层引用 
>> <div align='center'><a href='_formulas/demo/f_005.js.tex'><img src='_formulas/demo/f_005.svg'/></a></div>

7. 多层引用 (不规范)
>> <div align='center'><a href='_formulas/demo/f_006.js.tex'><img src='_formulas/demo/f_006.svg'/></a></div>

8. 更多示例
    <div align='center'><a href='_formulas/demo/f_007.js.tex'><img src='_formulas/demo/f_007.svg'/></a></div>
9. 删除
10. 更多示例

<div align='center'><a href='_formulas/demo/f_008.js.tex'><img src='_formulas/demo/f_008.svg'/></a></div>

### 不应该被识别的示例

1. a $1$ s
