#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
const {AllPackages} = require('mathjax-full/js/input/tex/AllPackages.js');

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);

const tex = new TeX({packages: AllPackages});
const svg = new SVG({fontCache: 'none'});
const html = mathjax.document('', {InputJax: tex, OutputJax: svg});

if (process.argv.length < 4) {
  console.error("用法: node tex2svg.js input.tex output.svg");
  process.exit(1);
}

const inputFile = path.resolve(process.argv[2]);
const outputFile = path.resolve(process.argv[3]);

if (!fs.existsSync(inputFile)) {
  console.error(`❌ 输入文件不存在: ${inputFile}`);
  process.exit(1);
}

let texSource;
try {
  texSource = fs.readFileSync(inputFile, 'utf8').trim();
  if (!texSource) {
    console.error(`❌ 输入文件为空: ${inputFile}`);
    process.exit(1);
  }
} catch (err) {
  console.error(`❌ 读取文件失败: ${inputFile}`);
  console.error(err.stack || err.message);
  process.exit(1);
}

try {
  const node = html.convert(texSource, {display: true});
  const svgElement = adaptor.firstChild(node);
  const svgOutput = adaptor.outerHTML(svgElement);

  // 检查 MathJax 是否插入了错误标记
  if (svgOutput.includes('data-mjx-error')) {
    console.error(svgOutput);
    console.error(`❌ 转换失败: ${inputFile} 中存在 MathJax 解析错误`);
    process.exit(1);
  }

  fs.writeFileSync(outputFile, svgOutput, 'utf8');
  console.log(`✅ 已生成: ${outputFile}`);
} catch (err) {
  console.error("❌ 转换失败");
  console.error(`输入文件: ${inputFile}`);
  console.error(`输出文件: ${outputFile}`);
  console.error("错误信息:", err.message);
  if (err.stack) {
    console.error("错误堆栈:\n", err.stack);
  }
  process.exit(1);
}
