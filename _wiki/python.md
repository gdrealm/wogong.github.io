---
title: python
date: 2014-06-10
update: 2018-03-07
---

## NOTE

1. `python -m SimpleHTTPServer` 8000端口快速共享文件。(Python3 中取消了SimpleHTTPServer 这个模块。)
2. 中文注释避免编码错误问题 `# -*- coding: utf-8 -*-`
3. module 导入
   - import module 推荐
   - from module import func 只导入需要的函数
   - from module import * 不推荐
4. itertools 迭代工具
5. ipython notebook
6. ipython
  dir() 查看当前导入的模块
7. requests docuemnt: http://docs.python-requests.org/en/master/
8. BeautifulSoup 还需要进一步学习，熟悉选择器的用法
9. `pip install $(pip list --outdated | awk '{ print $1 }') --upgrade`

## Project

1. moinmoin
   在线wiki。还不错。使用过一段时间，从vimwiki 迁移过来，后来再次迁移到gollum。
2. Python(x,y)
   用于科学计算
3. pelican
4. simiki
5. shadowsocks

## Basics

0. 注释，采用\#符号
1. function

        def func_name():
            statements

        lambda x: exp(x)

        lambda : exp(anything)

2. if

        if i==1:
            do something here
        elif i==0:
            do some other things
        else:
            just do

3. for

        for i in range(1,10,2):
            do something

## Scientific

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
   The cmath module provides many of the functions found in the math module, but these accept complex numbers.
3. NumPy & SciPy
    NumPy为Python提供了快速的多维数组处理的能力，而SciPy则在NumPy基础上添加了众多的科学计算所需的各种工具包，有了这两个库，Python就有几乎和Matlab一样的处理数据和计算的能力了。

    NumPy和SciPy官方网址： http://www.scipy.org

    NumPy为Python带来了真正的多维数组功能，并且提供了丰富的函数库处理这些数组。它将常用的数学函数都进行数组化，使得这些数学函数能够直接对数组进行操作，将本来需要在Python级别进行的循环，放到C语言的运算中，明显地提高了程序的运算速度。

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

## Vamei tutorial

作者：Vamei 出处：<http://www.cnblogs.com/vamei> 

### Python基础教程01 Hello World

### Python基础教程02 基本数据类型

变量不需要声明，不需要删除，可以直接回收适用。

type(): 查询数据类型

整数，浮点数，真值，字符串

### Python基础教程03 序列

tuple元素不可变，list元素可变

序列的引用 s[2], s[1:8:2], s[2:0:-1]

字符串是一种tuple

### Python基础教程04 运算

数学 +, -, *, /, **, %
判断 ==, !=, >, >=, <, <=, in
逻辑 and, or, not

### Python基础教程05 缩进和选择

if语句之后的冒号

以四个空格的缩进来表示隶属关系, Python中不能随意缩进

    if  <条件1>:

        statement

    elif <条件2>:

        statement

    elif <条件3>：

        statement

    else:

        statement

### Python基础教程06 循环

    range()

    python 3 list(range(5))

    for 元素 in 序列:

    while 条件:

    continue   # 在循环的某一次执行中，如果遇到continue, 那么跳过这一次执行，进行下一次的操作

    break      # 停止执行整个循环

### Python基础教程07 函数

    def square_sum(a,b):
    c = a**2 + b**2
    return c

### Python基础教程08 面向对象的基本概念

将东西根据属性归类 ( 将object归为class )

方法是一种属性，表示动作

用继承来说明父类-子类关系。子类自动具有父类的所有属性。

self代表了根据类定义而创建的对象，方法中第一个参数是 self

建立对一个对象： 对象名 = 类名()

引用对象的属性： object.attribute

### Python基础教程09 面向对象的进一步拓展

通过self调用类属性

    __init__(): 在建立对象时自动执行

类属性和对象的性质的区别

### Python基础教程10 反过头来看看

len() dir() help()

数据结构list(列表)是一个类。

运算符是方法

### Python进阶01 词典

词典的每个元素是键值对。元素没有顺序。

    dic = {'tom':11, 'sam':57,'lily':100}

    dic['tom'] = 99

    for key in dic: ...

    del, len()

### Python进阶02 文本文件的输入输出

Python具有基本的文本文件读写功能。Python的标准库提供有更丰富的读写功能。

文本文件的读写主要通过open()所构建的文件对象来实现。

1. 打开文件，创建文件对象。

    f = open(文件名，模式)

    "r"     # 只读
    "w"     # 写入

2. 文件对象的方法：

    读取方法：

        content = f.read(N)          # 读取N bytes的数据
        content = f.readline()       # 读取一行
        content = f.readlines()     # 读取所有行，储存在表中，每个元素是一行。

    写入方法：

        f.write('I like apple')  # 将'I like apple'写入文件
        f.write(list) # 将一个包含有多个字符串的表写入文件，每个元素成为文件中的一行。

    关闭文件：

        f.close()

3. 循环读入文件：

        for line in file(文件名):    print line
        # 利用file()函数，我们创建了一个循环对象。在循环中，文件的每一行依次被读取，赋予给line变量。

### Python进阶03 模块

我们之前看到了函数和对象。从本质上来说，它们都是为了更好的组织已经有的程序，以方便重复利用。

模块(module)也是为了同样的目的。在Python中，一个.py文件就构成一个模块。通过模块，你可以调用其它文件中的程序。

1. 引入(import)和使用模块

我们先写一个first.py文件，内容如下：

    def laugh():    print 'HaHaHaHa'

再写一个second.py

    import firstfor i in range(10):    first.laugh()

在second.py中，我们并没有定义laugh函数，但通过从first中引入(import)，我们就可以直接使用first.py中的laugh函数了。

从上面可以看到，引入模块后，我们可以通过 模块.对象 的方式来调用所想要使用的对象。上面例子中，first为引入的模块，laugh()是我们所引入的对象。

此外，还有其它的引入方式, import a as b, from a import ， 都是处于方便书写的原因，本质上没有差别。

2. 搜索路径

Python会在以下路径中搜索它想要寻找的模块：

    1. 程序所在的文件夹
    2. 标准库的安装路径
    3. 操作系统环境变量PYTHONPATH所包含的路径

如果你有自定义的模块，或者下载的模块，可以根据情况放在相应的路径，以便python可以找到。

3. 模块包

可以将功能相似的模块放在同一个文件夹（比如说dir）中，通过import dir.module的方式引入。

注意，该文件夹中必须包含一个__init__.py的文件，以便提醒python知道该文件夹为一个模块包。__init__.py可以是一个空文件。

总结

    import module

    module.object

    __init__.py

### Python进阶04 函数的参数对应

1. 关键字传递
2. 参数默认值
3. 包裹传递

        # list
        def func(*name):
        print type(name)
        print name

        func(1,4,6)
        func(5,6,7,1,2,3)

        # dict
        def func(**dict):
        print type(dict)
        print dict

        func(a=1,b=9)
        func(m=2,n=1,c=11)

4. 解包裹

        def func(a,b,c):
        print a,b,c

        args = (1,3,4)
        func(*args)

        dict = {'a':1,'b':2,'c':3}
        func(**dict)

5. 混合
    在定义或者调用参数时，参数的几种传递方式可以混合。但在过程中要小心前后顺序。基本原则是，先位置，再关键字，再包裹位置，再包裹关键字，并且根据上面所说的原理细细分辨。

### Python进阶05 循环设计

1. range()
2. enumerate()在每次循环中，返回的是一个包含两个元素的定值表(tuple)，两个元素分别赋予index和char
3. zip()函数的功能，就是从多个列表中，依次各取出一个元素。每次取出的(来自不同列表的)元素合成一个元组，合并成的元组放入zip()返回的列表中。zip()函数起到了聚合列表的功能。

    zip()
    zip(*zipped)

### Python进阶06 循环对象

### Python进阶07 函数对象

### usage

1. --user (recommend)

        # install to ~/.local
        pip install --user pkg_name

2. virtualenv

        sudo pip install virtualenv
        virtualenv NEW
        cd NEW
        source ./bin/activate
        pip list
        deactivate
        virtualenv -p /usr/bin/python2.7 ENV2.7
        * virtualenv --relocatable ./
        * pip freeze > requirements.txt
        pip install -r requirements.txt
        # ref: http://www.jianshu.com/p/08c657bd34f1

3. command

        pip install -U
        pip uninstall

## Mac 下的 Python 环境

系统自带：`/System/Library/Frameworks/Python.framework/Versions/2.7`
homebrew: `usr/local/Cellar/python3/`
homebrew: `usr/local/Cellar/python2/`
Anaconda
python 系统自带
python2 brew python2
python3 brew python3