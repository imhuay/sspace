LoRA (Low-Rank Adaptation)
===
<!--START_SECTION:badge-->
<!--END_SECTION:badge-->
<!--info
date: 2025-09-15 02:29:31
toc_title: LoRA
top: false
draft: false
hidden: true
section_number: false
level: 0
tag: []
-->

<!--START_SECTION:keywords-->
> ***Keywords**: LoRA*
<!--END_SECTION:keywords-->

<!--START_SECTION:paper_title-->
<!--END_SECTION:paper_title-->

<!--START_SECTION:toc-->
- [基础概念](#基础概念)
- [实践细节](#实践细节)
- [变体](#变体)
    - [QLoRA](#qlora)
    - [AdaLoRA](#adalora)
    - [DoLA](#dola)
<!--END_SECTION:toc-->

---

## 基础概念

- **背景**:
    <!-- - **全参数微调** 大型预训练模型 (如 LLaMA) 的 **训练成本** 极高, 为每个下游任务独立部署一个模型副本的 **存储开销** 巨大; -->
    - 对大型预训练模型 (如 LLaMA) 进行 **全参数微调** 的 **训练成本** 极高; 此外, 为每个下游任务存储一套独立的模型参数也会带来巨大的 **存储开销**;
- **核心假设 (低秩假设)**:
    <!-- - 研究发现, 模型在适应下游任务时, 并不需要在完整的 **高维空间** (权重矩阵 $W \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$) 中进行更新; 这个空间巨大, 参数极多; -->
    - 研究发现, 模型在适应下游任务时, 并 **不需要在完整的高维空间中更新权重矩阵** $W \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$;
    - 真正有效的更新具有明显 **结构和模式** (**低秩性/低秩结构**), 即 **微调过程中真正重要的变化是低维的**;
    - 这意味着在微调时, **权重更新矩阵** $\Delta W \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$ 可以用一个 **低秩分解** 来有效近似:
        $$
        \Delta W = B \cdot A
        $$
        其中 $B \in \mathbb{R}^{d_{\text{out}} \times r}, \quad A \in \mathbb{R}^{r \times d_{\text{in}}}$, 且 **秩** $r \ll \min(d_{\text{out}}, d_{\text{in}})$
    - **这个假设被实践证明是正确的**;
- **具体做法/思路**:
    - 基于上述 **低秩假设**, 对需要微调的 **线性层** (如 `nn.Linear`), **冻结其原始权重** $W_0$, **不直接计算其更新** $\Delta W_0 \in \mathbb{R}^{d_{\text{out}} \times d_{\text{in}}}$;
    - 而是 **参数化** 两个小矩阵 $B \in \mathbb{R}^{d_{\text{out}} \times r}$ 和 $A \in \mathbb{R}^{r \times d_{\text{in}}}$, 且 $r \ll \min(d_{\text{out}}, d_{\text{in}})$;
    - 然后通过 **旁路** 的方式学习一个低秩更新矩阵 $\Delta W = B \cdot A$, **间接模拟权重更新**;
    - **推理时**, 将低秩更新与原始权重合并/相加;
        - 为了在改变秩 $r$ 时灵活调整更新量/**控制更新幅度**, **避免重新调整学习率等训练超参**, 还会引入一个缩放因子 $\frac{\alpha}{r}$ 作用于低秩通路的输出 (**软约束**); 
        - **前向过程** 为:
        $$
        h = Wx + \frac{\alpha}{r} \Delta W x = Wx + \frac{\alpha}{r}B(Ax)
        $$

## 实践细节

- **初始化策略**:
    $$
    \Delta W = B \cdot A
    $$
    - $A$: **正态分布** 或 Kaiming/Xavier 初始化;
    - $B$: 全零，使训练开始时等价于无适配器（即使 $\Delta W = 0$）
    - **目的**: **保证训练稳定性** (训练开始时仅在原模型附近做微扰);
- **超参选择**:
    - $r$ (**秩**): 
        - 控制了更新子空间的参数量和表征能力;
        - **域内单一任务** 一般取 `4-16`; 
        - **指令/跨域任务** 可以取 `16-64` 或更高;
    - $\frac{\alpha}{r}$:
        - 一般取 $\alpha \approx r$, 简化训练时调参, 主要调学习率;
    - dropout:
        - LoRA 路径上的 dropout，缓解过拟合（如 0.05–0.2）;
- **放置位置**:
    - **注意力子层**: $W_q, W_k, W_v, W_o$；实践上分配到多处通常优于集中在单一矩阵;
    - **MLP 子层:** gate/up/down 投影;
        > LLaMA 中的 MLP 使用 **SwiGLU** 激活函数, 有三个子层:
        >> $\text{MLP}(x) = W_{\text{down}} \cdot (\text{Swish}(xW_{\text{gate}}) \otimes (xW_{\text{up}}))$
    - **归一化与嵌入层:** 很少, 主流收益集中在注意力与 MLP 层;
- **参数比例 (LoRA 参数 / 全量参数)**:
    $$
    \frac{r \times (d_{\text{in}}+d_{\text{out}})}{d_{\text{out}} \times d_{\text{in}}}
    $$
- **合并与可拔插**:
    - 推理时可将 $\Delta W$ 合并进 $W$ 得到 $W' = W + \frac{\alpha}{r} BA$，不增加推理延迟; 也可保持 **可拔插** 以多任务切换;

## 变体

### QLoRA
> 基座权重量化到 4-bit（如 NF4），LoRA 在低精度基座上训练，极致节省显存;

### AdaLoRA
> 动态分配每层 rank，将容量预算投向更“重要”的层;

### DoLA
> 将权重分解为幅度与方向，单独调整，有时更稳更准;


<!--START_SECTION:keyword-->
<!--keyword_info
name: ~~QLoRA~~
-->
<!--END_SECTION:keyword-->