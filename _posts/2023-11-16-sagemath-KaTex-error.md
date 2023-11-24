---
title: 解决sagemath Latex输出渲染错误
date: 2023-11-16 22:12:19
img_path: /_posts/
math: true
---

在jupyter notebook中使用sagemath，并且使用`%display latex`输出时，出现
> ParseError: KaTeX parse error: \newcommand{\Bold} attempting to redefine \Bold; use \renewcommand

解决

```python
from sage.misc.latex_macros import sage_configurable_latex_macros
global sage_configurable_latex_macros
marco = "\\newcommand{\\Bold}[1]{\\mathbf{#1}}"
if marco in sage_configurable_latex_macros: sage_configurable_latex_macros.remove(marco)
```
