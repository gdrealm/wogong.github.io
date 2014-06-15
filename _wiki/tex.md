---
layout: wiki
title: tex
update: 2014-06-13
---

相关条目： [[texmacs]]

1. 推荐文档书籍
- 《LaTeX2e 完全学习手册》
- lshort

2. 排版
一直想学而未坚持下来，总是在使用的时候为求方便叛逃
到Office阵营。其实Tex/LaTex并不是十分难学，前期
学习成本的确会高一点，但是之后的方便会证明这种投入
是值得的。加油！

- 关于中英文、数学公式混排中的标点符号选择问题。所
有文本段落使用全角逗号和空心句号，只有在数学式之中
的逗号为半角。

3. 安装 INSTALL
推荐TexLive 套装。目前使用的是Texlive2013 。Windows
与Linux 下均有相应的安装包，安装过程很简单。不推荐
采用源里面的安装，例如Arch `%sudo pacman -S texlive-core` ，
采用这种方式安装的Tex可能不包括常用的宏包，例如
ctex（后文会详细说到）。

xelatex + ctex
4. Tex 术语
    - format: tex; plain tex; latex(latex2e, latex3); context [CTeX资料](http://www.ctex.org/LaTeX)
    - engine: latex; pdflatex; xetex; luatex
    - macro package: 对基本格式的功能扩展
    - distro: 套件，各种引擎、宏包、文档的集合
    - 编译：tex ——> dvi/pdf



## 使用


中文推荐解决方案，ctex 文档类

### 数学排版
1. 2^x

### 常用命令

    latex example.tex_____nothing to say
    dvips example.dvi_____make .dvi into .ps
    xdvi example.dvi_____displsy .dvi(only for unix~)

### Latex宏包
- syntonly
- babel
- inputenc
- fontenc

### Latex内部命令

    \\ or \newline
    \\*   强行断行，禁止分页
    \newpage
    \sloppy
    \fussy
    \underline{text}  强调（划线）
    \emph{text}  强调（斜体）
    \mbox{text}
    \fbox{text}
    \frenchspacing
    \mbox{}  取消连字
    \tableofcontents
    \maketitle
    \title{...}
    \author{...\and...}
    \date{...}
    \frontmatter  应紧接\begin{document}，罗马数字页码
    \mainmatter  应在第一章正文紧前，阿拉伯数字页码重新计数
    \appendix
    \backmatter
    \label{marker},\ref{marker} and \pageref{marker}  交叉引用
    \footnote{text}
    \textit{text}
    \textsf{text}
    \texttt{text}
    \verb+text+
    
for style: article

    \section{...}
    \section**{...}  不出现在目录，不编号 (一个星号)
    \paragraph{...}
  
    \subsection{...}
    \subparagraph{...}
  
    \subsubsection{...}
  
    for style: report&book
    \part{...}
    \chapter{...}
  
Latex字符串:

    \today
    \TeX
    \LaTeX
    \LaTeXe
    


Latex特殊字符、符号:
''  ''
''
-  连字号
--  短破折号
--- 破折号
$-$  减号
\~  波浪号
$\sim$  波浪号
$^{\circ}\mathrm{C}$  度
\ldots  省略号



Latex环境：

    \begin{environment} text end{environment}
    itemize 简单列表
    enumerate  带序号的列表
    description  带描述的列表 
    note: text中使用item[]标识
  
    flushleft  左对齐文本
    flushright  右对齐
    center  中央对齐
  
    quote  一般引用
    quotation  较长引用，对段落进行缩进
    verse  引用诗歌
  
    verbatim  逐字打印
  
    tabular
  
