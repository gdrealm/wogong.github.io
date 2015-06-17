---
layout: wiki
title: python
date: 2014-06-10
update: 2015-03-04
---

## NOTE
1. `python -m SimpleHTTPServer` 8000端口快速共享文件。(Python3 中取消了SimpleHTTPServer 这个模块。)
3. 中文注释避免编码错误问题 `# -*- coding: utf-8 -*-`
3. module 导入
   - import module 推荐
   - from module import func 只导入需要的函数
   - from module import * 不推荐
2. itertools 迭代工具
5. ipython notebook (pythonxy)
    - linux 
        sudo apt-get install ipython-notebook
        sudo apt-get install python-matplotlib
6. v2ex_daily
    pip install BeautifulSoup4
    pip install requests

## INSTALL
Windows 下，建议安装32bit 版本。
### easy_install
[下载地址：](http://pypi.python.org/pypi/setuptools) 
可以找到正确的版本进行下载。win7 32位可以下载
setuptools-0.6c11.win32-py2.7.exe 。

注意：win7 64位必须使用ez_setup.py进行安装。方法
是下载
[ez_setup.py](http://peak.telecommunity.com/dist/ez_setup.py)
后，在cmd下执行 python ez_setup.py，
即可自动安装setuptools。目前没有直接的exe安装版本。

### vim 配置
pep8 编程风格检查；vim缩进折叠等设置见配置文件
flake8 同样也很神奇，但是暂时没必要安装

### pip
<http://pip.readthedocs.org/en/latest/installing.html>

sudo apt-get install python-pip
pip install 
pip install -U 安装更新
pip uninstall

## 相关项目
1. moinmoin  
   在线wiki。还不错。使用过一段时间，从vimwiki 迁移过来，后来再次迁移到gollum。
2. Python(x,y)
   用于科学计算
### Web 框架
1. web.py
2. 

## 基本语法
注释，采用\#符号
1. function

        def func_name():
            statements
        
        lambda x: exp(x)

2. if

        if i==1:
            do something here

3. for

        for i in range(1,10,2)
            do something

## 科学计算
0. core python
    - abs(a) Absolute value of a
    - max( sequence ) Largest element of sequence
    - min( sequence ) Smallest element of sequence
    - round(a,n) Round a to n decimal places
    - cmp(a,b) Returns −1 if a < b; 0 if a = b; 1 if a > b

### 函数库 module
1. math
   math.pi
   math.factorial
   math.pow
   math.exp
2. cmath
   The cmath module provides many of the functions found in the math module, but
these accept complex numbers.
3. NumPy & SciPy
    NumPy为Python提供了快速的多维数组处理的能力，而SciPy则在NumPy基础上添加了众多的科学
计算所需的各种工具包，有了这两个库，Python就有几乎和Matlab一样的处理数据和计算的能力了。
   
    NumPy和SciPy官方网址： http://www.scipy.org

    NumPy为Python带来了真正的多维数组功能，并且提供了丰富的函数库处理这些数组。它将常用的
数学函数都进行数组化，使得这些数学函数能够直接对数组进行操作，将本来需要在Python级别进行
的循环，放到C语言的运算中，明显地提高了程序的运算速度。
    
    SciPy的核心计算部分都是一些久经考验的Fortran数值计算库，例如：
    - 线性代数使用LAPACK库
    - 快速傅立叶变换使用FFTPACK库
    - 常微分方程求解使用ODEPACK库
    - 非线性方程组求解以及最小值求解等使用MINPACK库
4. SymPy
    SymPy官方网址： http://code.google.com/p/sympy
5. matplotlib

    # no X support
    import matplotlib
    matplotlib.use('Agg')

### 数值分析
1. 非线性方程与方程组的数值解法
   - `roots` 求解多项式的全部零点，转化为特征值问题求解。numpy, `from numpy import roots`
   - `fsolve` 非线性方程组求解。minpack 中的 hybrd, hybrj 算法。scipy.opimize
2. 符号计算 sympy
   - x = Symbol("x")
   - re 取实部
   - im 取虚部
   - series() Taylor 展开
   - pprint() pretty print
   - expand() 将函数展开部
3. 数值积分
   - trapz() 梯形公式 numpy
   - romberg(f,a,b,show=True) romberg 算法 scipy.integrate
   - quad() 自适应求积公式 QUADPACK scipy.integrate
   - dblauqd() 迭代使用quad()
   - tplquad()
   - nquad()

4. 数值微分

5. 常微分方程
   - odeint() scipy.integrate

6. 矩阵运算
   mat('1 2 3; 4 5 6')
   mat([[1,2,3],[4,5,6]])
   mat.I 逆
   mat.T 转置
