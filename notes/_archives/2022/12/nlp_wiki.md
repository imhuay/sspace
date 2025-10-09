NLP 领域术语 Wiki
===
<!--START_SECTION:badge-->
![create date](https://img.shields.io/static/v1?label=create%20date&message=2022-12-xx&labelColor=gray&color=lightsteelblue&style=flat-square)
![last modify](https://img.shields.io/static/v1?label=last%20modify&message=2025-07-08%2016%3A53%3A13&labelColor=gray&color=thistle&style=flat-square)
<!--END_SECTION:badge-->
<!--info
top: false
hidden_in_recent: false
-->

<!-- TOC -->
- [子词切分](#子词切分)
    - [相关工具库](#相关工具库)
    - [BPE](#bpe)
<!-- TOC -->

## 子词切分
> Subword Tokenization, 即将一个单词进一步切分为若干连续片段;

- NLP 领域中使用**无监督**的子词切分算法取代词形还原和词干提取来对词表进行压缩, 以缓解数据稀疏问题;
- 一个好的子词切分算法应该尽量将原词拆分成有意义或频繁使用的片段, 如 "annoyingly" -> "annoy" "ing" "ly";
- 在基于预训练的现代 NLP 任务中已经成为行业共识的基础步骤;
- 常见的子词切分算法: Byte-Pair Encoding ([BPE](#bpe)), Byte-level BPE, WordPiece, Unigram
    > [Subword tokenization - huggingface](https://huggingface.co/docs/transformers/tokenizer_summary#subword-tokenization)

### 相关工具库
- [huggingface/tokenizers: 💥 Fast State-of-the-Art Tokenizers optimized for Research and Production](https://github.com/huggingface/tokenizers)
- [google/sentencepiece: Unsupervised text tokenizer for Neural Network-based text generation.](https://github.com/google/sentencepiece)

### BPE
> 字节对编码 ([Byte Pair Encoding](https://en.wikipedia.org/wiki/Byte_pair_encoding), BPE)是一种基于统计的数据压缩算法;  

- [BPE 切分示例 - huggingface](https://huggingface.co/docs/transformers/tokenizer_summary#bytepair-encoding-bpe)
