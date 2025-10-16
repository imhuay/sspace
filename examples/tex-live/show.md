

<!--

<div align='center'><img src='path/to/xxx.png' height='300'/></div>

<details><summary><b>点击展开</b></summary>
</details>

[xxx - imhuay/studis](https://github.com/imhuay/studies/blob/master/notes/_archives/2022/04/xxx.md)

特殊符号:
  空格: <&nbsp;>
  • ◦ ▫ ▪ ∙(更小) ◉ ◎ ◇ ♦ ▷ ▶ ☐ ✓ ✕ ✗ ✘ ★ ☆ ♠ ♣ ♥ ♦ ✦ ✧ ✶ ⭒ ➢ ➔ ➜ ➤ › » → ‐ ⁃ ⌁
  → ⇒ ↦ ↔ ↝ ↜ ↠ ↣ ➔ ➙ ➛ ➜ ➞ ⟶ ➡ ➤ ➢ ➨ › » ▶ ▷ ∴ ∵ ⇨ ↦ ┈ ╌

Emoji:
  🚨⚠️🔔📌📍🎯🔖🏷️🚩💡🔦❗‼️💥🥢🔥✅☑️✔️⭕❌❓📔
  📝✨⏳🔍👀⏰🌠🌌🎈🎉🧨🎀🎫🎐🧣📢
  0️⃣ 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ 🔟 🔄 ⬆️ ⬇️ ⬅️ ➡️ ↔️

Latex 常用:
  空白符: '\hspace{1em}/{2pt}/{3cm}', '\quad', '\qquad', '\,', '\:', '\;'

-->

### 效果测试

$$
\begin{aligned}
f_t &= \sigma(W_f[h_{t-1},x_t] + b_t) \\
i_t &= \sigma(W_i[h_{t-1},x_t] + b_i) \\
\tilde{C}_t &= \tanh(W_C[h_{t-1},x_t] + b_C) \\
C_t &= f_t * C_{t-1} + i_t * \tilde{C}_t \\
o_t &= \sigma(W_o[h_{t-1},x_t] + b_o) \\
h_t &= o_t * \tanh(C_t)
\end{aligned}
$$

<div align='center'><img src='test_js.svg'/></div>

<!-- 
node scripts/tex2svg.js examples/tex-live/test_js.tex examples/tex-live/test_js.svg
 -->