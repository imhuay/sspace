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

const inputFile = process.argv[2];
const outputFile = process.argv[3];
const texSource = fs.readFileSync(inputFile, 'utf8').trim();

try {
  const node = html.convert(texSource, {display: true});
  // 关键：只取 <svg> 节点
  const svgElement = adaptor.firstChild(node);  
  const svgOutput = adaptor.outerHTML(svgElement);

  fs.writeFileSync(outputFile, svgOutput, 'utf8');
  console.log(`✅ 已生成: ${path.resolve(outputFile)}`);
} catch (err) {
  console.error("❌ 转换失败:", err.message);
  process.exit(1);
}
